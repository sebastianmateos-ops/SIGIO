from datetime import date

from sqlalchemy.orm import Session

from app.models.beneficiario import Beneficiario
from app.models.categoria import Categoria
from app.models.estado_implemento import EstadoImplemento
from app.models.implemento import Implemento
from app.models.prestamo import Prestamo


class ReporteRepository:

    @staticmethod
    def listar_inventario(
        db: Session,
        categoria_id: int | None = None,
        estado_id: int | None = None,
        activo: bool | None = None,
    ) -> list[dict]:

        query = (
            db.query(
                Implemento,
                Categoria,
                EstadoImplemento,
            )
            .join(
                Categoria,
                Implemento.categoria_id == Categoria.id,
            )
            .join(
                EstadoImplemento,
                Implemento.estado_id == EstadoImplemento.id,
            )
        )

        if categoria_id is not None:
            query = query.filter(
                Implemento.categoria_id == categoria_id
            )

        if estado_id is not None:
            query = query.filter(
                Implemento.estado_id == estado_id
            )

        if activo is not None:
            query = query.filter(
                Implemento.activo == activo
            )

        implementos = (
            query
            .order_by(
                Categoria.nombre,
                Implemento.codigo,
            )
            .all()
        )

        resultado = []

        for implemento, categoria, estado in implementos:

            resultado.append(
                {
                    "codigo": implemento.codigo,
                    "categoria": categoria.nombre,
                    "estado": estado.nombre,
                    "marca": implemento.marca,
                    "modelo": implemento.modelo,
                    "ubicacion": implemento.ubicacion,
                    "activo": implemento.activo,
                }
            )

        return resultado

    @staticmethod
    def listar_prestamos(
        db: Session,
        beneficiario_id: int | None = None,
        implemento_id: int | None = None,
        activo: bool | None = None,
        fecha_desde: date | None = None,
        fecha_hasta: date | None = None,
    ) -> list[dict]:

        query = (
            db.query(
                Prestamo,
                Beneficiario,
                Implemento,
                Categoria,
            )
            .join(
                Beneficiario,
                Prestamo.beneficiario_id == Beneficiario.id,
            )
            .join(
                Implemento,
                Prestamo.implemento_id == Implemento.id,
            )
            .join(
                Categoria,
                Implemento.categoria_id == Categoria.id,
            )
        )

        if beneficiario_id is not None:
            query = query.filter(
                Prestamo.beneficiario_id == beneficiario_id
            )

        if implemento_id is not None:
            query = query.filter(
                Prestamo.implemento_id == implemento_id
            )

        if activo is not None:
            query = query.filter(
                Prestamo.activo == activo
            )

        if fecha_desde is not None:
            query = query.filter(
                Prestamo.fecha_prestamo >= fecha_desde
            )

        if fecha_hasta is not None:
            query = query.filter(
                Prestamo.fecha_prestamo <= fecha_hasta
            )

        prestamos = (
            query
            .order_by(
                Prestamo.fecha_prestamo.desc(),
            )
            .all()
        )

        resultado = []

        for (
            prestamo,
            beneficiario,
            implemento,
            categoria,
        ) in prestamos:

            resultado.append(
                {
                    "numero": prestamo.numero,
                    "fecha_prestamo": prestamo.fecha_prestamo,
                    "fecha_prevista_devolucion": prestamo.fecha_prevista_devolucion,
                    "fecha_devolucion": prestamo.fecha_devolucion,
                    "beneficiario": beneficiario.nombre_completo,
                    "documento": beneficiario.documento,
                    "implemento": implemento.codigo,
                    "categoria": categoria.nombre,
                    "activo": prestamo.activo,
                    "observaciones": prestamo.observaciones,
                }
            )

        return resultado