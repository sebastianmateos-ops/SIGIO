from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.adquisicion import (
    AdquisicionCreate,
    AdquisicionResponse,
)
from app.security.dependencies import (
    get_current_active_user,
)
from app.services.adquisicion_service import (
    AdquisicionService,
)

router = APIRouter(
    prefix="/adquisiciones",
    tags=["Adquisiciones"],
)


@router.get(
    "",
    response_model=list[AdquisicionResponse],
    summary="Listar adquisiciones",
)
def listar_adquisiciones(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    return AdquisicionService.listar(db)


@router.get(
    "/{adquisicion_id}",
    response_model=AdquisicionResponse,
    summary="Obtener adquisición",
)
def obtener_adquisicion(
    adquisicion_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    adquisicion = AdquisicionService.obtener(
        db,
        adquisicion_id,
    )

    if adquisicion is None:

        raise HTTPException(
            status_code=404,
            detail="Adquisición no encontrada.",
        )

    return adquisicion


@router.post(
    "",
    response_model=AdquisicionResponse,
    status_code=201,
    summary="Registrar adquisición",
)
def crear_adquisicion(
    datos: AdquisicionCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    try:

        return AdquisicionService.crear(
            db,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )