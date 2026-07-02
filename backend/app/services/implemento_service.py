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
from app.schemas.implemento import ImplementoCreate


class ImplementoService:

    @staticmethod
    def listar(db: Session) -> list[Implemento]:
        return ImplementoRepository.listar(db)

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
    def validar_categoria(
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
        """
        Crea un nuevo implemento.
        """

        categoria = ImplementoService.validar_categoria(
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

        implemento = ImplementoRepository.crear(
            db,
            implemento,
        )

        return implemento