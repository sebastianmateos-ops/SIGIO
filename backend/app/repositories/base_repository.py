from typing import Generic, TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """
    Repositorio base para operaciones CRUD.
    """

    def __init__(self, model: type[T]):
        self.model = model

    def listar(
        self,
        db: Session,
    ) -> list[T]:

        return (
            db.query(self.model)
            .all()
        )

    def obtener_por_id(
        self,
        db: Session,
        entity_id: int,
    ) -> T | None:

        return (
            db.query(self.model)
            .filter(
                self.model.id == entity_id
            )
            .first()
        )

    def agregar(
        self,
        db: Session,
        entity: T,
    ) -> None:
        """
        Agrega una entidad a la sesión.
        No realiza commit.
        """

        db.add(entity)

    def actualizar(
        self,
        db: Session,
        entity: T,
    ) -> None:
        """
        La entidad ya está asociada a la sesión.
        El commit queda a cargo del Service.
        """

        pass

    def eliminar(
        self,
        db: Session,
        entity: T,
    ) -> None:
        """
        Elimina una entidad.
        No realiza commit.
        """

        db.delete(entity)

    def refrescar(
        self,
        db: Session,
        entity: T,
    ) -> None:

        db.refresh(entity)