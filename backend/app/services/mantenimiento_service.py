from datetime import datetime

from sqlalchemy.orm import Session

from app.models.mantenimiento import Mantenimiento
from app.repositories.estado_implemento_repository import (
    EstadoImplementoRepository,
)
from app.repositories.implemento_repository import (
    ImplementoRepository,
)
from app.repositories.mantenimiento_repository import (
    MantenimientoRepository,
)
from app.schemas.mantenimiento import (
    MantenimientoCreate,
    MantenimientoSalida,
)


class MantenimientoService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Mantenimiento]:

        return MantenimientoRepository.listar(db)

    @staticmethod
    def obtener(
        db: Session,
        mantenimiento_id: int,
    ) -> Mantenimiento | None:

        return MantenimientoRepository.obtener_por_id(
            db,
            mantenimiento_id,
        )

    @staticmethod
    def crear(
        db: Session,
        datos: MantenimientoCreate,
        usuario_id: int,
    ) -> Mantenimiento:

        implemento = ImplementoRepository.obtener_por_id(
            db,
            datos.implemento_id,
        )

        if implemento is None:
            raise ValueError(
                "El implemento no existe."
            )

        mantenimiento_activo = (
            MantenimientoRepository.obtener_mantenimiento_activo(
                db,
                datos.implemento_id,
            )
        )

        if mantenimiento_activo is not None:
            raise ValueError(
                "El implemento ya se encuentra en mantenimiento."
            )

        estado = EstadoImplementoRepository.obtener_por_codigo(
            db,
            "MANT",
        )

        if estado is None:
            raise ValueError(
                "No existe el estado MANT."
            )

        mantenimiento = Mantenimiento(
            implemento_id=datos.implemento_id,
            usuario_ingreso_id=usuario_id,
            motivo=datos.motivo,
            observaciones=datos.observaciones,
        )

        implemento.estado_id = estado.id

        db.add(mantenimiento)
        db.commit()
        db.refresh(mantenimiento)

        return mantenimiento

    @staticmethod
    def finalizar(
        db: Session,
        mantenimiento_id: int,
        datos: MantenimientoSalida,
        usuario_id: int,
    ) -> Mantenimiento:

        mantenimiento = (
            MantenimientoRepository.obtener_por_id(
                db,
                mantenimiento_id,
            )
        )

        if mantenimiento is None:
            raise ValueError(
                "Mantenimiento inexistente."
            )

        if mantenimiento.estado != "EN_MANTENIMIENTO":
            raise ValueError(
                "El mantenimiento ya fue finalizado."
            )

        implemento = ImplementoRepository.obtener_por_id(
            db,
            mantenimiento.implemento_id,
        )

        estado = EstadoImplementoRepository.obtener_por_codigo(
            db,
            "DISP",
        )

        if implemento is None or estado is None:
            raise ValueError(
                "Error interno."
            )

        mantenimiento.estado = "FINALIZADO"
        mantenimiento.fecha_salida = datetime.utcnow()
        mantenimiento.usuario_salida_id = usuario_id
        mantenimiento.observaciones = datos.observaciones

        implemento.estado_id = estado.id

        db.commit()
        db.refresh(mantenimiento)

        return mantenimiento

    @staticmethod
    def eliminar(
        db: Session,
        mantenimiento: Mantenimiento,
    ) -> None:

        MantenimientoRepository.eliminar(
            db,
            mantenimiento,
        )