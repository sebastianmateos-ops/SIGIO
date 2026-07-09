from sqlalchemy.orm import Session

from app.core.config import settings

from app.models.categoria import Categoria
from app.models.implemento import Implemento

from app.repositories.categoria_repository import CategoriaRepository
from app.repositories.estado_implemento_repository import (
    EstadoImplementoRepository,
)
from app.repositories.implemento_repository import (
    ImplementoRepository,
)

from app.schemas.implemento import (
    ImplementoCreate,
    ImplementoListItem,
)


class ImplementoService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[ImplementoListItem]:

        implementos = ImplementoRepository.listar(db)

        return [
            ImplementoListItem(
                id=i.id,
                codigo=i.codigo,
                categoria=i.categoria.nombre,
                marca=i.marca,
                modelo=i.modelo,
                estado=i.estado.nombre,
                ubicacion=i.ubicacion,
            )
            for i in implementos
        ]

    @staticmethod
    def obtener(
        db: Session,
        implemento_id: int,
    ) -> Implemento | None:

        return ImplementoRepository.obtener_por_id(
            db,
            implemento_id,
        )

    @staticmethod
    def _validar_categoria(
        db: Session,
        categoria_id: int,
    ) -> Categoria:

        categoria = CategoriaRepository.obtener_por_id(
            db,
            categoria_id,
        )

        if categoria is None:
            raise ValueError(
                "La categoría no existe."
            )

        return categoria

    @staticmethod
    def _generar_codigo(
        db: Session,
        categoria: Categoria,
    ) -> str:

        ultimo = (
            ImplementoRepository.obtener_ultimo_por_categoria(
                db,
                categoria.id,
            )
        )

        if ultimo is None:
            correlativo = 1
        else:
            correlativo = (
                int(ultimo.codigo.split("-")[-1]) + 1
            )

        return (
            f"{settings.INVENTORY_PREFIX}"
            f"-{categoria.codigo}"
            f"-{correlativo:04d}"
        )

    @staticmethod
    def crear(
        db: Session,
        datos: ImplementoCreate,
    ) -> Implemento:

        categoria = ImplementoService._validar_categoria(
            db,
            datos.categoria_id,
        )

        estado = (
            EstadoImplementoRepository.obtener_por_codigo(
                db,
                "DISP",
            )
        )

        if estado is None:
            raise ValueError(
                "No existe el estado inicial 'DISP'."
            )

        codigo = ImplementoService._generar_codigo(
            db,
            categoria,
        )

        implemento = Implemento(
            codigo=codigo,
            categoria_id=categoria.id,
            estado_id=estado.id,
            marca=datos.marca,
            modelo=datos.modelo,
            numero_serie=datos.numero_serie,
            valor_estimado=datos.valor_estimado,
            ubicacion=datos.ubicacion,
            observaciones=datos.observaciones,
        )

        return ImplementoRepository.crear(
            db,
            implemento,
        )