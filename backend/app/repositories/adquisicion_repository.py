from sqlalchemy.orm import Session

from app.models.adquisicion import Adquisicion


class AdquisicionRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Adquisicion]:

        return (
            db.query(Adquisicion)
            .order_by(
                Adquisicion.fecha.desc(),
                Adquisicion.numero.desc(),
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        adquisicion_id: int,
    ) -> Adquisicion | None:

        return (
            db.query(Adquisicion)
            .filter(
                Adquisicion.id == adquisicion_id
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Adquisicion | None:

        return (
            db.query(Adquisicion)
            .filter(
                Adquisicion.uuid == uuid
            )
            .first()
        )

    @staticmethod
    def obtener_por_numero(
        db: Session,
        numero: str,
    ) -> Adquisicion | None:

        return (
            db.query(Adquisicion)
            .filter(
                Adquisicion.numero == numero
            )
            .first()
        )

    @staticmethod
    def obtener_ultima(
        db: Session,
    ) -> Adquisicion | None:

        return (
            db.query(Adquisicion)
            .order_by(
                Adquisicion.id.desc()
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        adquisicion: Adquisicion,
    ) -> Adquisicion:

        db.add(adquisicion)
        db.flush()
        db.refresh(adquisicion)

        return adquisicion

    @staticmethod
    def eliminar(
        db: Session,
        adquisicion: Adquisicion,
    ) -> None:

        db.delete(adquisicion)
        db.commit()