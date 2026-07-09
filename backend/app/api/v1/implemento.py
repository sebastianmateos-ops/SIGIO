from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.implemento import (
    ImplementoCreate,
    ImplementoListItem,
    ImplementoResponse,
)
from app.security.dependencies import (
    get_current_active_user,
)
from app.services.implemento_service import (
    ImplementoService,
)

router = APIRouter(
    prefix="/implementos",
    tags=["Implementos"],
)


@router.get(
    "",
    response_model=list[ImplementoListItem],
    summary="Listar implementos",
    description="Obtiene la lista de implementos para visualización.",
)
def listar_implementos(
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    return ImplementoService.listar(db)


@router.get(
    "/{implemento_id}",
    response_model=ImplementoResponse,
    summary="Obtener implemento por ID",
)
def obtener_implemento(
    implemento_id: int,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    implemento = ImplementoService.obtener(
        db,
        implemento_id,
    )

    if implemento is None:
        raise HTTPException(
            status_code=404,
            detail="Implemento no encontrado.",
        )

    return implemento


@router.post(
    "",
    response_model=ImplementoResponse,
    status_code=201,
    summary="Crear implemento",
)
def crear_implemento(
    datos: ImplementoCreate,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    try:
        return ImplementoService.crear(
            db,
            datos,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )