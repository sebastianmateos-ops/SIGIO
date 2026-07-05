from sqlalchemy.orm import Session

from app.models.estado_implemento import EstadoImplemento
from app.repositories.base_repository import BaseRepository


class EstadoImplementoRepository(BaseRepository[EstadoImplemento]):
    """
    Repositorio de estados de implemento.
    """

    def __init__(self):
        super().__init__(EstadoImplemento)

    def obtener_por_codigo(
        self,
        db: Session,
        codigo: str,
    ) -> EstadoImplemento | None:

        return (
            db.query(EstadoImplemento)
            .filter(
                EstadoImplemento.codigo == codigo
            )
            .first()
        )

    def obtener_por_nombre(
        self,
        db: Session,
        nombre: str,
    ) -> EstadoImplemento | None:

        return (
            db.query(EstadoImplemento)
            .filter(
                EstadoImplemento.nombre == nombre
            )
            .first()
        )