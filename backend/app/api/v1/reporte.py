from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.reporte import (
    ReporteInventarioFiltro,
    ReporteInventarioItem,
    ReportePrestamoFiltro,
    ReportePrestamoItem,
)
from app.security.dependencies import get_current_active_user
from app.services.reporte_service import ReporteService

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"],
)


@router.get(
    "/inventario",
    response_model=list[ReporteInventarioItem],
    summary="Reporte de Inventario General",
)
def reporte_inventario(
    filtro: ReporteInventarioFiltro = Depends(),
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    return ReporteService.inventario(
        db=db,
        filtro=filtro,
    )


@router.get(
    "/prestamos",
    response_model=list[ReportePrestamoItem],
    summary="Reporte de Préstamos",
)
def reporte_prestamos(
    filtro: ReportePrestamoFiltro = Depends(),
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    return ReporteService.prestamos(
        db=db,
        filtro=filtro,
    )