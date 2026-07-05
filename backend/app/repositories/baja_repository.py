from sqlalchemy.orm import Session

from app.models.baja import Baja


class BajaRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Baja]:

        return (
            db.query(Baja)
            .order_by(
                Baja.fecha.desc(),
                Baja.numero.desc(),
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        baja_id: int,
    ) -> Baja | None:

        return (
            db.query(Baja)
            .filter(
                Baja.id == baja_id
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Baja | None:

        return (
            db.query(Baja)
            .filter(
                Baja.uuid == uuid
            )
            .first()
        )

    @staticmethod
    def obtener_por_numero(
        db: Session,
        numero: str,
    ) -> Baja | None:

        return (
            db.query(Baja)
            .filter(
                Baja.numero == numero
            )
            .first()
        )

    @staticmethod
    def obtener_por_implemento(
        db: Session,
        implemento_id: int,
    ) -> Baja | None:

        return (
            db.query(Baja)
            .filter(
                Baja.implemento_id == implemento_id
            )
            .first()
        )

    @staticmethod
    def obtener_ultima(
        db: Session,
    ) -> Baja | None:

        return (
            db.query(Baja)
            .order_by(
                Baja.id.desc()
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        baja: Baja,
    ) -> Baja:

        db.add(baja)
        db.flush()
        db.refresh(baja)

        return baja

    @staticmethod
    def eliminar(
        db: Session,
        baja: Baja,
    ) -> None:

        db.delete(baja)
        db.commit()