from sqlalchemy.orm import Session

from app.models.beneficiario import Beneficiario
from app.models.implemento import Implemento
from app.models.prestamo import Prestamo

from app.repositories.beneficiario_repository import (
    BeneficiarioRepository,
)
from app.repositories.estado_implemento_repository import (
    EstadoImplementoRepository,
)
from app.repositories.implemento_repository import (
    ImplementoRepository,
)
from app.repositories.prestamo_repository import (
    PrestamoRepository,
)

from app.schemas.prestamo import (
    PrestamoCreate,
    PrestamoUpdate,
)

from datetime import UTC, datetime

from app.schemas.prestamo import PrestamoDevolucion


class PrestamoService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Prestamo]:

        return PrestamoRepository.listar(db)

    @staticmethod
    def obtener(
        db: Session,
        prestamo_id: int,
    ) -> Prestamo | None:

        return PrestamoRepository.obtener_por_id(
            db,
            prestamo_id,
        )

    @staticmethod
    def crear(
        db: Session,
        datos: PrestamoCreate,
        usuario_entrega_id: int,
    ) -> Prestamo:

        beneficiario = BeneficiarioRepository.obtener_por_id(
            db,
            datos.beneficiario_id,
        )

        if beneficiario is None:
            raise ValueError(
                "El beneficiario no existe."
            )

        implemento = ImplementoRepository.obtener_por_id(
            db,
            datos.implemento_id,
        )

        if implemento is None:
            raise ValueError(
                "El implemento no existe."
            )

        estado_disponible = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "DISP",
            )
        )

        if estado_disponible is None:
            raise ValueError(
                "No existe el estado DISP."
            )

        if implemento.estado_id != estado_disponible.id:
            raise ValueError(
                "El implemento no se encuentra disponible."
            )

        if PrestamoRepository.existe_prestamo_activo(
            db,
            implemento.id,
        ):
            raise ValueError(
                "El implemento ya posee un préstamo activo."
            )

        estado_prestado = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "PRES",
            )
        )

        if estado_prestado is None:
            raise ValueError(
                "No existe el estado PRES."
            )

        numero = PrestamoRepository.generar_numero(
            db,
        )

        prestamo = Prestamo(
            numero=numero,
            beneficiario_id=beneficiario.id,
            implemento_id=implemento.id,
            usuario_entrega_id=usuario_entrega_id,
            fecha_prevista_devolucion=datos.fecha_prevista_devolucion,
            observaciones=datos.observaciones,
            estado="ACTIVO",
        )

        try:

            db.add(prestamo)

            implemento.estado_id = estado_prestado.id

            db.commit()

            db.refresh(prestamo)

            return prestamo

        except Exception:

            db.rollback()

            raise

    @staticmethod
    def actualizar(
        db: Session,
        prestamo: Prestamo,
        datos: PrestamoUpdate,
    ) -> Prestamo:

        if datos.fecha_prevista_devolucion is not None:
            prestamo.fecha_prevista_devolucion = (
                datos.fecha_prevista_devolucion
            )

        if datos.fecha_devolucion is not None:
            prestamo.fecha_devolucion = (
                datos.fecha_devolucion
            )

        if datos.estado is not None:
            prestamo.estado = datos.estado

        if datos.observaciones is not None:
            prestamo.observaciones = datos.observaciones

        return PrestamoRepository.actualizar(
            db,
            prestamo,
        )

    @staticmethod
    def eliminar(
        db: Session,
        prestamo: Prestamo,
    ) -> None:

        PrestamoRepository.eliminar(
            db,
            prestamo,
        )

    @staticmethod
    def devolver(
        db: Session,
        prestamo_id: int,
        datos: PrestamoDevolucion,
        usuario_id: int,
    ) -> Prestamo:
        """
        Registra la devolución de un préstamo.
        """

        prestamo = PrestamoRepository.obtener_activo_por_id(
            db,
            prestamo_id,
        )

        if prestamo is None:
            raise ValueError(
                "El préstamo no existe o ya fue devuelto."
            )

        estado_disponible = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "DISP",
            )
        )

        if estado_disponible is None:
            raise ValueError(
                "No existe el estado DISP."
            )

        implemento = ImplementoRepository.obtener_por_id(
            db,
            prestamo.implemento_id,
        )

        if implemento is None:
            raise ValueError(
                "El implemento no existe."
            )

        try:

            prestamo.estado = "DEVUELTO"

            prestamo.fecha_devolucion = datetime.now(
                UTC,
            )

            prestamo.usuario_devolucion_id = usuario_id

            prestamo.observaciones = datos.observaciones

            implemento.estado_id = estado_disponible.id

            db.commit()

            db.refresh(prestamo)
            db.refresh(implemento)

            return prestamo

        except Exception:

            db.rollback()

            raise