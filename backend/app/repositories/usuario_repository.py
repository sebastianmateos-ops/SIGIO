from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository[Usuario]):
    """
    Repositorio de usuarios.
    """

    def __init__(self):
        super().__init__(Usuario)

    def obtener_por_usuario(
        self,
        db: Session,
        usuario: str,
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(
                Usuario.usuario == usuario
            )
            .first()
        )

    def obtener_por_email(
        self,
        db: Session,
        email: str,
    ) -> Usuario | None:

        return (
            db.query(Usuario)
            .filter(
                Usuario.email == email
            )
            .first()
        )