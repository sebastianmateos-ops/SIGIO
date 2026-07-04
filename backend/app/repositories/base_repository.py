from typing import Generic, TypeVar

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Repositorio base reutilizable.

    Implementa las operaciones CRUD comunes para todos los
    los repositorios del sistema SIGIO.

    No debe contener reglas de negocio.
    """

    def __init__(
        self,
        model: type[ModelType],
    ):
        self.model = model

    def listar(
        self,
        db: Session,
    ) -> list[ModelType]:
        """
        Obtiene todos los registros.
        """
        return db.scalars(
            select(self.model)
        ).all()

    def obtener(
        self,
        db: Session,
        registro_id: int,
    ) -> ModelType | None:
        """
        Obtiene un registro por su ID.
        """
        return db.get(
            self.model,
            registro_id,
        )

    def obtener_por_uuid(
        self,
        db: Session,
        uuid: str,
    ) -> ModelType | None:
        """
        Obtiene un registro por UUID.
        """
        return db.scalar(
            select(self.model).where(
                self.model.uuid == uuid
            )
        )

    def crear(
        self,
        db: Session,
        objeto: ModelType,
    ) -> ModelType:
        """
        Inserta un nuevo registro.
        """
        db.add(objeto)
        db.commit()
        db.refresh(objeto)

        return objeto

    def actualizar(
        self,
        db: Session,
        objeto: ModelType,
    ) -> ModelType:
        """
        Guarda los cambios realizados.
        """
        db.commit()
        db.refresh(objeto)

        return objeto

    def eliminar(
        self,
        db: Session,
        objeto: ModelType,
    ) -> None:
        """
        Elimina un registro.
        """
        db.delete(objeto)
        db.commit()

    def contar(
        self,
        db: Session,
    ) -> int:
        """
        Devuelve la cantidad de registros.
        """
        return db.scalar(
            select(func.count())
            .select_from(self.model)
        ) or 0

    def existe(
        self,
        db: Session,
        registro_id: int,
    ) -> bool:
        """
        Verifica si existe un registro.
        """
        return (
            self.obtener(
                db,
                registro_id,
            )
            is not None
        )