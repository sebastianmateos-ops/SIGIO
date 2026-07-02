from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import LoginRequest, Token
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"],
)


@router.post("/login", response_model=Token)
def login(
    dados: LoginRequest,
    db: Session = Depends(get_db),
):

    token = AuthService.login(
        db,
        dados.usuario,
        dados.password,
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos",
        )

    return {
        "access_token": token,
        "token_type": "bearer",
    }