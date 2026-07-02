from sqlalchemy.orm import Session

from app.models.categoria import Categoria


class CategoriaRepository:

    @staticmethod
    def obtener_por_id(
        db: Session,
        categoria_id: int,
    ) -> Categoria | None:

        return (
            db.query(Categoria)
            .filter(Categoria.id == categoria_id)
            .first()
        )

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Categoria]:

        return (
            db.query(Categoria)
            .order_by(Categoria.nombre)
            .all()
        )