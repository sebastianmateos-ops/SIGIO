from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.adquisicion import Adquisicion
from app.models.baja import Baja
from app.models.beneficiario import Beneficiario
from app.models.estado_implemento import EstadoImplemento
from app.models.implemento import Implemento
from app.models.mantenimiento import Mantenimiento
from app.models.prestamo import Prestamo


class DashboardRepository:

    @staticmethod
    def contar_implementos(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Implemento.id))
            .scalar()
            or 0
        )

    @staticmethod
    def contar_por_estado(
        db: Session,
        codigo_estado: str,
    ) -> int:

        return (
            db.query(func.count(Implemento.id))
            .join(
                EstadoImplemento,
                Implemento.estado_id == EstadoImplemento.id,
            )
            .filter(
                EstadoImplemento.codigo == codigo_estado
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_beneficiarios(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Beneficiario.id))
            .filter(
                Beneficiario.activo.is_(True)
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_prestamos_activos(
        db: Session,
    ) -> int:

        estado_prestado = (
            db.query(EstadoImplemento.id)
            .filter(
                EstadoImplemento.codigo == "PRES"
            )
            .scalar()
        )

        if estado_prestado is None:
            return 0

        return (
            db.query(func.count(Prestamo.id))
            .join(
                Implemento,
                Prestamo.implemento_id == Implemento.id,
            )
            .filter(
                Implemento.estado_id == estado_prestado
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_prestamos_finalizados(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Prestamo.id))
            .filter(
                Prestamo.activo.is_(False)
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_mantenimientos_activos(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Mantenimiento.id))
            .filter(
                Mantenimiento.estado == "EN_MANTENIMIENTO"
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_mantenimientos_finalizados(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Mantenimiento.id))
            .filter(
                Mantenimiento.estado == "FINALIZADO"
            )
            .scalar()
            or 0
        )

    @staticmethod
    def contar_adquisiciones(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Adquisicion.id))
            .scalar()
            or 0
        )

    @staticmethod
    def contar_bajas(
        db: Session,
    ) -> int:

        return (
            db.query(func.count(Baja.id))
            .scalar()
            or 0
        )