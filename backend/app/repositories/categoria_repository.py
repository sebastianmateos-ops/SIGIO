from sqlalchemy.orm import Session

from app.models.categoria import Categoria
from app.repositories.base_repository import BaseRepository


class CategoriaRepository(BaseRepository[Categoria]):
    """
    Repositorio de categorías.
    """

    def __init__(self):
        super().__init__(Categoria)

    def obtener_por_codigo(
        self,
        db: Session,
        codigo: str,
    ) -> Categoria | None:

        return (
            db.query(Categoria)
            .filter(Categoria.codigo == codigo)
            .first()
        )