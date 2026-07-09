from sqlalchemy.orm import Session

from app.repositories.categoria_repository import (
    CategoriaRepository,
)
from app.schemas.categoria import CategoriaResponse


class CategoriaService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[CategoriaResponse]:

        categorias = CategoriaRepository.listar(db)

        return [
            CategoriaResponse.model_validate(categoria)
            for categoria in categorias
        ]