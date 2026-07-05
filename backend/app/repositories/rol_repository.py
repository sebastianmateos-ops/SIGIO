from sqlalchemy.orm import Session

from app.models.rol import Rol


class RolRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Rol]:

        return (
            db.query(Rol)
            .order_by(Rol.nombre)
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        rol_id: int,
    ) -> Rol | None:

        return (
            db.query(Rol)
            .filter(Rol.id == rol_id)
            .first()
        )

    @staticmethod
    def obtener_por_nombre(
        db: Session,
        nombre: str,
    ) -> Rol | None:

        return (
            db.query(Rol)
            .filter(Rol.nombre == nombre)
            .first()
        )