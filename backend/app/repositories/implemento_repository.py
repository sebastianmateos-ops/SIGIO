from sqlalchemy.orm import Session

from app.models.implemento import Implemento


class ImplementoRepository:

    @staticmethod
    def listar(db: Session) -> list[Implemento]:
        return (
            db.query(Implemento)
            .order_by(Implemento.codigo)
            .all()
        )

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
    def obtener_por_id(
        db: Session,
        implemento_id: int,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(Implemento.id == implemento_id)
            .first()
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
    def crear(
        db: Session,
        implemento: Implemento,
    ) -> Implemento:

        db.add(implemento)
        db.commit()
        db.refresh(implemento)

        return implemento

    @staticmethod
    def actualizar(
        db: Session,
        implemento: Implemento,
    ) -> Implemento:

        db.commit()
        db.refresh(implemento)

        return implemento

    @staticmethod
    def eliminar(
        db: Session,
        implemento: Implemento,
    ):

        db.delete(implemento)
        db.commit()