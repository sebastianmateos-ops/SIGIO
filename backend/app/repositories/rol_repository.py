from sqlalchemy.orm import Session

from app.models.rol import Rol


class RolRepository:

    @staticmethod
    def obtener_por_nombre(db: Session, nombre: str) -> Rol | None:
        return (
            db.query(Rol)
            .filter(Rol.nombre == nombre)
            .first()
        )

    @staticmethod
    def crear(db: Session, rol: Rol) -> Rol:
        db.add(rol)
        db.commit()
        db.refresh(rol)
        return rol