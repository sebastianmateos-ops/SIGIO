from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.security.jwt import decode_access_token

API_PREFIX = "/api/v1"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{API_PREFIX}/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    """
    Obtiene el usuario autenticado a partir del JWT.
    """

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado.",
        )

    username = payload.get("sub")

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido.",
        )

    usuario = UsuarioRepository.obtener_por_usuario(
        db,
        username,
    )

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado.",
        )

    return usuario


def get_current_active_user(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """
    Verifica que el usuario autenticado se encuentre activo.
    """

    if not current_user.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario está inactivo.",
        )

    return current_user

def require_roles(
    *roles: str,
):
    """
    Verifica que el usuario autenticado posea
    alguno de los roles permitidos.
    """

    def role_checker(
        current_user: Usuario = Depends(
            get_current_active_user,
        ),
    ) -> Usuario:

        if current_user.rol.nombre not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tiene permisos para realizar esta acción.",
            )

        return current_user

    return role_checker