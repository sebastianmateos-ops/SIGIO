from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.usuario import Usuario
from app.schemas.dashboard import DashboardResponse
from app.security.dependencies import get_current_active_user
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=DashboardResponse,
    summary="Dashboard ejecutivo",
)
def obtener_dashboard(
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):

    return DashboardService.obtener_dashboard(db)