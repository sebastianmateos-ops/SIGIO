from sqlalchemy.orm import Session

from app.models.estado_implemento import EstadoImplemento


class EstadoImplementoRepository:

    @staticmethod
    def obtener_por_id(
        db: Session,
        estado_id: int,
    ) -> EstadoImplemento | None:

        return (
            db.query(EstadoImplemento)
            .filter(EstadoImplemento.id == estado_id)
            .first()
        )

    @staticmethod
    def obtener_por_codigo(
        db: Session,
        codigo: str,
    ) -> EstadoImplemento | None:

        return (
            db.query(EstadoImplemento)
            .filter(EstadoImplemento.codigo == codigo)
            .first()
        )

    @staticmethod
    def obtener_por_nombre(
        db: Session,
        nombre: str,
    ) -> EstadoImplemento | None:

        return (
            db.query(EstadoImplemento)
            .filter(EstadoImplemento.nombre == nombre)
            .first()
        )

    @staticmethod
    def listar(
        db: Session,
    ) -> list[EstadoImplemento]:

        return (
            db.query(EstadoImplemento)
            .order_by(EstadoImplemento.nombre)
            .all()
        )