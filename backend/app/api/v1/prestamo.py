from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.usuario import Usuario

from app.schemas.prestamo import (
    PrestamoCreate,
    PrestamoResponse,
    PrestamoUpdate,
)

from app.security.dependencies import (
    get_current_user,
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
    description="Obtiene la lista de préstamos.",
)
def listar_prestamos(
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return PrestamoService.listar(db)


@router.get(
    "/activos",
    response_model=list[PrestamoResponse],
    summary="Listar préstamos activos",
    description="Obtiene la lista de préstamos activos.",
)
def listar_prestamos_activos(
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return PrestamoService.listar_activos(db)


@router.get(
    "/{prestamo_id}",
    response_model=PrestamoResponse,
    summary="Obtener préstamo",
    description="Obtiene un préstamo por su ID.",
)
def obtener_prestamo(
    prestamo_id: int,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return PrestamoService.obtener(
            db,
            prestamo_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "",
    response_model=PrestamoResponse,
    status_code=201,
    summary="Registrar préstamo",
    description="Registra un nuevo préstamo.",
)
def crear_prestamo(
    datos: PrestamoCreate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return PrestamoService.crear(
            db,
            datos,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/{prestamo_id}/devolucion",
    response_model=PrestamoResponse,
    summary="Registrar devolución",
    description="Registra la devolución de un implemento prestado.",
)
def registrar_devolucion(
    prestamo_id: int,
    datos: PrestamoUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return PrestamoService.registrar_devolucion(
            db,
            prestamo_id,
            datos,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )