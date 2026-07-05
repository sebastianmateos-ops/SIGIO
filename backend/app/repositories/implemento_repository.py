from sqlalchemy.orm import Session

from app.models.implemento import Implemento
from app.repositories.base_repository import BaseRepository


class ImplementoRepository(BaseRepository[Implemento]):

    def __init__(self):
        super().__init__(Implemento)


    @staticmethod
    def listar_por_categoria(
        db: Session,
        categoria_id: int,
    ) -> list[Implemento]:

        return (
            db.query(Implemento)
            .filter(
                Implemento.categoria_id == categoria_id
            )
            .order_by(Implemento.codigo)
            .all()
        )

    @staticmethod
    def obtener_por_codigo(
        db: Session,
        codigo: str,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(Implemento.codigo == codigo)
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(Implemento.uuid == uuid)
            .first()
        )

    @staticmethod
    def obtener_ultimo_por_categoria(
        db: Session,
        categoria_id: int,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(
                Implemento.categoria_id == categoria_id
            )
            .order_by(Implemento.codigo.desc())
            .first()
        )
    
    @staticmethod
    def actualizar_estado(
        db: Session,
        implemento: Implemento,
        estado_id: int,
    ) -> None:
        """
        Actualiza el estado del implemento.

        No realiza commit.
        La transacción será controlada por el Service.
        """

        implemento.estado_id = estado_id