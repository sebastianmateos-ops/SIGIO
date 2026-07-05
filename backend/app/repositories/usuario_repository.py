from sqlalchemy.orm import Session

from app.models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Usuario]:

        return (
            db.query(Usuario)
            .order_by(Usuario.usuario)
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        usuario_id: int,
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(Usuario.id == usuario_id)
            .first()
        )

    @staticmethod
    def obtener_por_usuario(
        db: Session,
        usuario: str,
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(Usuario.usuario == usuario)
            .first()
        )

    @staticmethod
    def obtener_por_email(
        db: Session,
        email: str,
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(Usuario.email == email)
            .first()
        )