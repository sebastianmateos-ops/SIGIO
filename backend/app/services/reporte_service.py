from sqlalchemy.orm import Session

from app.repositories.reporte_repository import ReporteRepository
from app.schemas.reporte import (
    ReporteInventarioFiltro,
    ReporteInventarioItem,
    ReportePrestamoFiltro,
    ReportePrestamoItem,
)


class ReporteService:

    @staticmethod
    def inventario(
        db: Session,
        filtro: ReporteInventarioFiltro,
    ) -> list[ReporteInventarioItem]:

        datos = ReporteRepository.listar_inventario(
            db=db,
            categoria_id=filtro.categoria_id,
            estado_id=filtro.estado_id,
            activo=filtro.activo,
        )

        return [
            ReporteInventarioItem(**item)
            for item in datos
        ]

    @staticmethod
    def prestamos(
        db: Session,
        filtro: ReportePrestamoFiltro,
    ) -> list[ReportePrestamoItem]:

        datos = ReporteRepository.listar_prestamos(
            db=db,
            beneficiario_id=filtro.beneficiario_id,
            implemento_id=filtro.implemento_id,
            activo=filtro.activo,
            fecha_desde=filtro.fecha_desde,
            fecha_hasta=filtro.fecha_hasta,
        )

        return [
            ReportePrestamoItem(**item)
            for item in datos
        ]