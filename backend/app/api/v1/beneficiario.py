from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.usuario import Usuario

from app.schemas.beneficiario import (
    BeneficiarioCreate,
    BeneficiarioResponse,
    BeneficiarioUpdate,
)

from app.security.dependencies import (
    get_current_user,
)

from app.services.beneficiario_service import (
    BeneficiarioService,
)

router = APIRouter(
    prefix="/beneficiarios",
    tags=["Beneficiarios"],
)


@router.get(
    "",
    response_model=list[BeneficiarioResponse],
    summary="Listar beneficiarios",
    description="Obtiene la lista de todos los beneficiarios registrados.",
)
def listar_beneficiarios(
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return BeneficiarioService.listar(db)


@router.get(
    "/buscar",
    response_model=list[BeneficiarioResponse],
    summary="Buscar beneficiarios",
    description="Busca beneficiarios por nombre, apellido o documento.",
)
def buscar_beneficiarios(
    texto: str = Query(
        ...,
        min_length=2,
        description="Texto a buscar.",
    ),
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return BeneficiarioService.buscar(
        db,
        texto,
    )


@router.get(
    "/{beneficiario_id}",
    response_model=BeneficiarioResponse,
    summary="Obtener beneficiario",
    description="Obtiene un beneficiario por su ID.",
)
def obtener_beneficiario(
    beneficiario_id: int,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return BeneficiarioService.obtener(
            db,
            beneficiario_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "",
    response_model=BeneficiarioResponse,
    status_code=201,
    summary="Crear beneficiario",
    description="Registra un nuevo beneficiario.",
)
def crear_beneficiario(
    datos: BeneficiarioCreate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return BeneficiarioService.crear(
            db,
            datos,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.put(
    "/{beneficiario_id}",
    response_model=BeneficiarioResponse,
    summary="Actualizar beneficiario",
    description="Actualiza la información de un beneficiario.",
)
def actualizar_beneficiario(
    beneficiario_id: int,
    datos: BeneficiarioUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        return BeneficiarioService.actualizar(
            db,
            beneficiario_id,
            datos,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{beneficiario_id}",
    status_code=204,
    summary="Eliminar beneficiario",
    description="Elimina un beneficiario del sistema.",
)
def eliminar_beneficiario(
    beneficiario_id: int,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        BeneficiarioService.eliminar(
            db,
            beneficiario_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )