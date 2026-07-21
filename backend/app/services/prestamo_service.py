from datetime import date

from sqlalchemy.orm import Session

from app.models.prestamo import Prestamo

from app.repositories.prestamo_repository import (
    PrestamoRepository,
)

from app.repositories.implemento_repository import (
    ImplementoRepository,
)

from app.repositories.beneficiario_repository import (
    BeneficiarioRepository,
)

from app.repositories.estado_implemento_repository import (
    EstadoImplementoRepository,
)

from app.schemas.prestamo import (
    PrestamoCreate,
    PrestamoUpdate,
)


class PrestamoService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Prestamo]:

        return PrestamoRepository.listar(db)

    @staticmethod
    def listar_activos(
        db: Session,
    ) -> list[Prestamo]:

        return PrestamoRepository.listar_activos(db)

    @staticmethod
    def obtener(
        db: Session,
        prestamo_id: int,
    ) -> Prestamo:

        return PrestamoService._obtener_prestamo(
            db,
            prestamo_id,
        )

    @staticmethod
    def _obtener_prestamo(
        db: Session,
        prestamo_id: int,
    ) -> Prestamo:

        prestamo = PrestamoRepository.obtener_por_id(
            db,
            prestamo_id,
        )

        if prestamo is None:
            raise ValueError(
                "Préstamo no encontrado."
            )

        return prestamo

    @staticmethod
    def crear(
        db: Session,
        datos: PrestamoCreate,
    ) -> Prestamo:

        implemento = (
            ImplementoRepository.obtener_por_id(
                db,
                datos.implemento_id,
            )
        )

        if implemento is None:
            raise ValueError(
                "Implemento no encontrado."
            )

        beneficiario = (
            BeneficiarioRepository.obtener_por_id(
                db,
                datos.beneficiario_id,
            )
        )

        if beneficiario is None:
            raise ValueError(
                "Beneficiario no encontrado."
            )

        estado_disponible = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "DISP",
            )
        )

        estado_prestado = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "PRES",
            )
        )

        if estado_disponible is None:
            raise ValueError(
                "No existe el estado DISP."
            )

        if estado_prestado is None:
            raise ValueError(
                "No existe el estado PRES."
            )

        if implemento.estado_id != estado_disponible.id:
            raise ValueError(
                "El implemento no está disponible."
            )

        prestamo_activo = (
            PrestamoRepository.obtener_prestamo_activo_por_implemento(
                db,
                implemento.id,
            )
        )

        if prestamo_activo is not None:
            raise ValueError(
                "El implemento ya posee un préstamo activo."
            )

        prestamo = Prestamo(
            implemento_id=datos.implemento_id,
            beneficiario_id=datos.beneficiario_id,
            fecha_prestamo=datos.fecha_prestamo,
            observaciones=datos.observaciones,
            activo=True,
        )

        prestamo = PrestamoRepository.crear(
            db,
            prestamo,
        )

        implemento.estado_id = estado_prestado.id

        ImplementoRepository.actualizar(
            db,
            implemento,
        )

        return prestamo

    @staticmethod
    def registrar_devolucion(
        db: Session,
        prestamo_id: int,
        datos: PrestamoUpdate,
    ) -> Prestamo:

        prestamo = (
            PrestamoService._obtener_prestamo(
                db,
                prestamo_id,
            )
        )

        if prestamo.fecha_devolucion is not None:
            raise ValueError(
                "El préstamo ya fue devuelto."
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

        prestamo.fecha_devolucion = (
            datos.fecha_devolucion
            or date.today()
        )

        prestamo.observaciones = (
            datos.observaciones
        )

        prestamo = PrestamoRepository.actualizar(
            db,
            prestamo,
        )

        implemento = prestamo.implemento

        implemento.estado_id = estado_disponible.id

        ImplementoRepository.actualizar(
            db,
            implemento,
        )

        return prestamo

    @staticmethod
    def eliminar(
        db: Session,
        prestamo_id: int,
    ) -> None:

        prestamo = (
            PrestamoService._obtener_prestamo(
                db,
                prestamo_id,
            )
        )

        PrestamoRepository.eliminar(
            db,
            prestamo,
        )