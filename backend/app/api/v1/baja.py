from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.baja import (
    BajaCreate,
    BajaResponse,
)
from app.security.dependencies import (
    get_current_active_user,
)
from app.services.baja_service import (
    BajaService,
)

router = APIRouter(
    prefix="/bajas",
    tags=["Bajas"],
)


@router.get(
    "",
    response_model=list[BajaResponse],
    summary="Listar bajas",
)
def listar_bajas(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    return BajaService.listar(db)


@router.get(
    "/{baja_id}",
    response_model=BajaResponse,
    summary="Obtener baja",
)
def obtener_baja(
    baja_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    baja = BajaService.obtener(
        db,
        baja_id,
    )

    if baja is None:

        raise HTTPException(
            status_code=404,
            detail="Baja no encontrada.",
        )

    return baja


@router.post(
    "",
    response_model=BajaResponse,
    status_code=201,
    summary="Registrar baja",
)
def crear_baja(
    datos: BajaCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    try:

        return BajaService.crear(
            db,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )