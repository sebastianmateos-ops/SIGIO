from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.mantenimiento import (
    MantenimientoCreate,
    MantenimientoResponse,
    MantenimientoSalida,
)
from app.security.dependencies import (
    get_current_active_user,
)
from app.services.mantenimiento_service import (
    MantenimientoService,
)

router = APIRouter(
    prefix="/mantenimientos",
    tags=["Mantenimientos"],
)


@router.get(
    "",
    response_model=list[MantenimientoResponse],
    summary="Listar mantenimientos",
)
def listar_mantenimientos(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return MantenimientoService.listar(db)


@router.get(
    "/{mantenimiento_id}",
    response_model=MantenimientoResponse,
    summary="Obtener mantenimiento",
)
def obtener_mantenimiento(
    mantenimiento_id: int,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    mantenimiento = MantenimientoService.obtener(
        db,
        mantenimiento_id,
    )

    if mantenimiento is None:
        raise HTTPException(
            status_code=404,
            detail="Mantenimiento no encontrado.",
        )

    return mantenimiento


@router.post(
    "",
    response_model=MantenimientoResponse,
    status_code=201,
    summary="Ingresar implemento a mantenimiento",
)
def crear_mantenimiento(
    datos: MantenimientoCreate,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    try:

        return MantenimientoService.crear(
            db,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/{mantenimiento_id}/finalizar",
    response_model=MantenimientoResponse,
    summary="Finalizar mantenimiento",
)
def finalizar_mantenimiento(
    mantenimiento_id: int,
    datos: MantenimientoSalida,
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    try:

        return MantenimientoService.finalizar(
            db,
            mantenimiento_id,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )