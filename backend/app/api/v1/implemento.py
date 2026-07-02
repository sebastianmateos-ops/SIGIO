from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.implemento import ImplementoResponse
from app.services.implemento_service import ImplementoService

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