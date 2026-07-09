from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.categoria import CategoriaResponse
from app.security.dependencies import (
    get_current_active_user,
)
from app.services.categoria_service import (
    CategoriaService,
)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"],
)


@router.get(
    "",
    response_model=list[CategoriaResponse],
    summary="Listar categorías",
    description="Obtiene todas las categorías disponibles.",
)
def listar_categorias(
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    return CategoriaService.listar(db)