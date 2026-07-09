from sqlalchemy.orm import Session, joinedload

from app.models.implemento import Implemento


class ImplementoRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Implemento]:

        return (
            db.query(Implemento)
            .options(
                joinedload(Implemento.categoria),
                joinedload(Implemento.estado),
            )
            .filter(
                Implemento.activo.is_(True),
            )
            .order_by(
                Implemento.codigo,
            )
            .all()
        )

    @staticmethod
    def listar_por_categoria(
        db: Session,
        categoria_id: int,
    ) -> list[Implemento]:

        return (
            db.query(Implemento)
            .options(
                joinedload(Implemento.categoria),
                joinedload(Implemento.estado),
            )
            .filter(
                Implemento.activo.is_(True),
                Implemento.categoria_id == categoria_id,
            )
            .order_by(
                Implemento.codigo,
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        implemento_id: int,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .options(
                joinedload(Implemento.categoria),
                joinedload(Implemento.estado),
            )
            .filter(
                Implemento.id == implemento_id,
            )
            .first()
        )

    @staticmethod
    def obtener_por_codigo(
        db: Session,
        codigo: str,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(
                Implemento.codigo == codigo,
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Implemento | None:

        return (
            db.query(Implemento)
            .filter(
                Implemento.uuid == uuid,
            )
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
                Implemento.categoria_id == categoria_id,
            )
            .order_by(
                Implemento.codigo.desc(),
            )
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
    ) -> None:

        db.delete(implemento)
        db.commit()

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