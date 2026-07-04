from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.prestamo import Prestamo


class PrestamoRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        prestamo_id: int,
    ) -> Prestamo | None:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.id == prestamo_id,
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Prestamo | None:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.uuid == uuid,
            )
            .first()
        )

    @staticmethod
    def generar_numero(
        db: Session,
    ) -> str:
        """
        Genera el siguiente número de préstamo.

        Ejemplo:
            PR-00000001
        """

        ultimo_id = db.query(
            func.max(
                Prestamo.id,
            )
        ).scalar()

        siguiente = (
            1
            if ultimo_id is None
            else ultimo_id + 1
        )

        return f"PR-{siguiente:08d}"

    @staticmethod
    def existe_prestamo_activo(
        db: Session,
        implemento_id: int,
    ) -> bool:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.implemento_id == implemento_id,
                Prestamo.estado == "ACTIVO",
                Prestamo.activo.is_(True),
            )
            .first()
            is not None
        )

    @staticmethod
    def obtener_prestamo_activo(
        db: Session,
        implemento_id: int,
    ) -> Prestamo | None:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.implemento_id == implemento_id,
                Prestamo.estado == "ACTIVO",
                Prestamo.activo.is_(True),
            )
            .first()
        )

    @staticmethod
    def listar_activos(
        db: Session,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.estado == "ACTIVO",
                Prestamo.activo.is_(True),
            )
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

    @staticmethod
    def listar_vencidos(
        db: Session,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.estado == "VENCIDO",
                Prestamo.activo.is_(True),
            )
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

    @staticmethod
    def historial_implemento(
        db: Session,
        implemento_id: int,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.implemento_id == implemento_id,
            )
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

    @staticmethod
    def crear(
        db: Session,
        prestamo: Prestamo,
    ) -> Prestamo:

        db.add(prestamo)
        db.commit()
        db.refresh(prestamo)

        return prestamo

    @staticmethod
    def actualizar(
        db: Session,
        prestamo: Prestamo,
    ) -> Prestamo:

        db.commit()
        db.refresh(prestamo)

        return prestamo

    @staticmethod
    def eliminar(
        db: Session,
        prestamo: Prestamo,
    ) -> None:

        db.delete(prestamo)
        db.commit()