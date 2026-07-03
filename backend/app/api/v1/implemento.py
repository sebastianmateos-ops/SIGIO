from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.implemento import (
    ImplementoCreate,
    ImplementoResponse,
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
    response_model=list[ImplementoResponse],
)
def listar_implementos(
    db: Session = Depends(get_db),
):
    return ImplementoService.listar(db)


@router.get(
    "/{implemento_id}",
    response_model=ImplementoResponse,
)
def obtener_implemento(
    implemento_id: int,
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
)
def crear_implemento(
    datos: ImplementoCreate,
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