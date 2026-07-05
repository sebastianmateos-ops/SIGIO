from sqlalchemy.orm import Session

from app.models.mantenimiento import Mantenimiento


class MantenimientoRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Mantenimiento]:

        return (
            db.query(Mantenimiento)
            .order_by(
                Mantenimiento.fecha_ingreso.desc()
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        mantenimiento_id: int,
    ) -> Mantenimiento | None:

        return (
            db.query(Mantenimiento)
            .filter(
                Mantenimiento.id == mantenimiento_id
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Mantenimiento | None:

        return (
            db.query(Mantenimiento)
            .filter(
                Mantenimiento.uuid == uuid
            )
            .first()
        )

    @staticmethod
    def listar_por_implemento(
        db: Session,
        implemento_id: int,
    ) -> list[Mantenimiento]:

        return (
            db.query(Mantenimiento)
            .filter(
                Mantenimiento.implemento_id == implemento_id
            )
            .order_by(
                Mantenimiento.fecha_ingreso.desc()
            )
            .all()
        )

    @staticmethod
    def obtener_mantenimiento_activo(
        db: Session,
        implemento_id: int,
    ) -> Mantenimiento | None:

        return (
            db.query(Mantenimiento)
            .filter(
                Mantenimiento.implemento_id == implemento_id,
                Mantenimiento.estado == "EN_MANTENIMIENTO",
                Mantenimiento.activo.is_(True),
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        mantenimiento: Mantenimiento,
    ) -> Mantenimiento:

        db.add(mantenimiento)
        db.commit()
        db.refresh(mantenimiento)

        return mantenimiento

    @staticmethod
    def actualizar(
        db: Session,
        mantenimiento: Mantenimiento,
    ) -> Mantenimiento:

        db.commit()
        db.refresh(mantenimiento)

        return mantenimiento

    @staticmethod
    def eliminar(
        db: Session,
        mantenimiento: Mantenimiento,
    ) -> None:

        db.delete(mantenimiento)
        db.commit()