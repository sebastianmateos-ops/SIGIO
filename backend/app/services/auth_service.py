from sqlalchemy.orm import Session

from app.repositories.usuario_repository import UsuarioRepository
from app.security.hash import verify_password
from app.security.jwt import create_access_token


class AuthService:

    @staticmethod
    def login(db: Session, usuario: str, password: str):

        usuario_db = UsuarioRepository.obtener_por_usuario(
            db,
            usuario,
        )

        if usuario_db is None:
            return None

        if not verify_password(
            password,
            usuario_db.password_hash,
        ):
            return None

        token = create_access_token(
            {"sub": usuario_db.usuario}
        )

        return token