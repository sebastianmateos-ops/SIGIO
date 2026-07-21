from sqlalchemy.orm import Session, joinedload

from app.models.prestamo import Prestamo


class PrestamoRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .options(
                joinedload(Prestamo.implemento),
                joinedload(Prestamo.beneficiario),
            )
            .filter(
                Prestamo.activo.is_(True),
            )
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

    @staticmethod
    def listar_activos(
        db: Session,
    ) -> list[Prestamo]:

        return (
            db.query(Prestamo)
            .options(
                joinedload(Prestamo.implemento),
                joinedload(Prestamo.beneficiario),
            )
            .filter(
                Prestamo.fecha_devolucion.is_(None),
                Prestamo.activo.is_(True),
            )
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
            .options(
                joinedload(Prestamo.implemento),
                joinedload(Prestamo.beneficiario),
            )
            .filter(
                Prestamo.id == prestamo_id,
            )
            .first()
        )

    @staticmethod
    def obtener_prestamo_activo_por_implemento(
        db: Session,
        implemento_id: int,
    ) -> Prestamo | None:

        return (
            db.query(Prestamo)
            .filter(
                Prestamo.implemento_id == implemento_id,
                Prestamo.fecha_devolucion.is_(None),
                Prestamo.activo.is_(True),
            )
            .first()
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

        prestamo.activo = False

        db.commit()
        db.refresh(prestamo)