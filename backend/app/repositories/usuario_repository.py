from sqlalchemy.orm import Session

from app.models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def obtener_por_usuario(db: Session, usuario: str) -> Usuario | None:
        return (
            db.query(Usuario)
            .filter(Usuario.usuario == usuario)
            .first()
        )

    @staticmethod
    def obtener_por_id(db: Session, usuario_id: int) -> Usuario | None:
        return (
            db.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .first()
        )

    @staticmethod
    def crear(db: Session, usuario: Usuario) -> Usuario:
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario