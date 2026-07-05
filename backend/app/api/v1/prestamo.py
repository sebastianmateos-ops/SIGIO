from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario

from app.schemas.prestamo import (
    PrestamoCreate,
    PrestamoDevolucion,
    PrestamoResponse,
    PrestamoUpdate,
)

from app.security.dependencies import (
    get_current_active_user,
)

from app.services.prestamo_service import (
    PrestamoService,
)

router = APIRouter(
    prefix="/prestamos",
    tags=["Préstamos"],
)


@router.get(
    "",
    response_model=list[PrestamoResponse],
    summary="Listar préstamos",
)
def listar_prestamos(
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    return PrestamoService.listar(db)


@router.get(
    "/{prestamo_id}",
    response_model=PrestamoResponse,
    summary="Obtener préstamo",
)
def obtener_prestamo(
    prestamo_id: int,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    prestamo = PrestamoService.obtener(
        db,
        prestamo_id,
    )

    if prestamo is None:
        raise HTTPException(
            status_code=404,
            detail="Préstamo no encontrado.",
        )

    return prestamo


@router.post(
    "",
    response_model=PrestamoResponse,
    status_code=201,
    summary="Crear préstamo",
)
def crear_prestamo(
    datos: PrestamoCreate,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    try:

        return PrestamoService.crear(
            db,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/{prestamo_id}",
    response_model=PrestamoResponse,
    summary="Actualizar préstamo",
)
def actualizar_prestamo(
    prestamo_id: int,
    datos: PrestamoUpdate,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    prestamo = PrestamoService.obtener(
        db,
        prestamo_id,
    )

    if prestamo is None:
        raise HTTPException(
            status_code=404,
            detail="Préstamo no encontrado.",
        )

    return PrestamoService.actualizar(
        db,
        prestamo,
        datos,
    )


@router.delete(
    "/{prestamo_id}",
    status_code=204,
    summary="Eliminar préstamo",
)
def eliminar_prestamo(
    prestamo_id: int,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    prestamo = PrestamoService.obtener(
        db,
        prestamo_id,
    )

    if prestamo is None:
        raise HTTPException(
            status_code=404,
            detail="Préstamo no encontrado.",
        )

    PrestamoService.eliminar(
        db,
        prestamo,
    )

    return None


@router.post(
    "/{prestamo_id}/devolver",
    response_model=PrestamoResponse,
    summary="Registrar devolución",
    description="Registra la devolución de un implemento prestado.",
)
def devolver_prestamo(
    prestamo_id: int,
    datos: PrestamoDevolucion,
    current_user: Usuario = Depends(
        get_current_active_user,
    ),
    db: Session = Depends(get_db),
):
    try:

        return PrestamoService.devolver(
            db,
            prestamo_id,
            datos,
            current_user.id,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )