from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository
from app.schemas.dashboard import (
    DashboardAdquisiciones,
    DashboardBajas,
    DashboardBeneficiarios,
    DashboardMantenimientos,
    DashboardPrestamos,
    DashboardResponse,
    DashboardResumen,
)


class DashboardService:

    @staticmethod
    def obtener_dashboard(
        db: Session,
    ) -> DashboardResponse:

        resumen = DashboardResumen(
            total_implementos=DashboardRepository.contar_implementos(db),
            disponibles=DashboardRepository.contar_por_estado(
                db,
                "DISP",
            ),
            prestados=DashboardRepository.contar_por_estado(
                db,
                "PRES",
            ),
            mantenimiento=DashboardRepository.contar_por_estado(
                db,
                "MANT",
            ),
            bajas=DashboardRepository.contar_por_estado(
                db,
                "BAJA",
            ),
        )

        beneficiarios = DashboardBeneficiarios(
            activos=DashboardRepository.contar_beneficiarios(db),
        )

        prestamos = DashboardPrestamos(
            activos=DashboardRepository.contar_prestamos_activos(db),
            finalizados=DashboardRepository.contar_prestamos_finalizados(db),
        )

        mantenimientos = DashboardMantenimientos(
            activos=DashboardRepository.contar_mantenimientos_activos(db),
            finalizados=DashboardRepository.contar_mantenimientos_finalizados(db),
        )

        adquisiciones = DashboardAdquisiciones(
            total=DashboardRepository.contar_adquisiciones(db),
        )

        bajas = DashboardBajas(
            total=DashboardRepository.contar_bajas(db),
        )

        return DashboardResponse(
            resumen=resumen,
            beneficiarios=beneficiarios,
            prestamos=prestamos,
            mantenimientos=mantenimientos,
            adquisiciones=adquisiciones,
            bajas=bajas,
        )