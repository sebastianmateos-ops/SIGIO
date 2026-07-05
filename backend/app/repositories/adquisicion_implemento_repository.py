from sqlalchemy.orm import Session

from app.models.adquisicion_implemento import (
    AdquisicionImplemento,
)


class AdquisicionImplementoRepository:

    @staticmethod
    def listar_por_adquisicion(
        db: Session,
        adquisicion_id: int,
    ) -> list[AdquisicionImplemento]:

        return (
            db.query(AdquisicionImplemento)
            .filter(
                AdquisicionImplemento.adquisicion_id == adquisicion_id
            )
            .all()
        )

    @staticmethod
    def obtener_por_implemento(
        db: Session,
        implemento_id: int,
    ) -> AdquisicionImplemento | None:

        return (
            db.query(AdquisicionImplemento)
            .filter(
                AdquisicionImplemento.implemento_id == implemento_id
            )
            .first()
        )

    @staticmethod
    def crear(
        db: Session,
        detalle: AdquisicionImplemento,
    ) -> AdquisicionImplemento:

        db.add(detalle)
        db.flush()

        return detalle