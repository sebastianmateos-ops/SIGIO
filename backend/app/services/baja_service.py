from sqlalchemy.orm import Session

from app.models.baja import Baja
from app.repositories.baja_repository import BajaRepository
from app.repositories.estado_implemento_repository import (
    EstadoImplementoRepository,
)
from app.repositories.implemento_repository import (
    ImplementoRepository,
)
from app.schemas.baja import BajaCreate


class BajaService:

    TIPOS_BAJA = {
        "DESGASTE",
        "ROTURA",
        "OBSOLETO",
        "PERDIDA",
        "DONACION",
        "OTRO",
    }

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Baja]:

        return BajaRepository.listar(db)

    @staticmethod
    def obtener(
        db: Session,
        baja_id: int,
    ) -> Baja | None:

        return BajaRepository.obtener_por_id(
            db,
            baja_id,
        )

    @classmethod
    def crear(
        cls,
        db: Session,
        datos: BajaCreate,
        usuario_id: int,
    ) -> Baja:

        cls._validar_tipo_baja(
            datos.tipo_baja,
        )

        implemento = ImplementoRepository.obtener_por_id(
            db,
            datos.implemento_id,
        )

        if implemento is None:
            raise ValueError(
                "Implemento inexistente."
            )

        existe = BajaRepository.obtener_por_implemento(
            db,
            implemento.id,
        )

        if existe is not None:
            raise ValueError(
                f"El implemento {implemento.codigo} ya fue dado de baja."
            )

        estado_baja = (
            EstadoImplementoRepository()
            .obtener_por_codigo(
                db,
                "BAJA",
            )
        )

        if estado_baja is None:
            raise ValueError(
                "No existe el estado BAJA."
            )

        if implemento.estado_id != estado_baja.id:

            estado_anterior = implemento.estado_id

        else:

            raise ValueError(
                "El implemento ya está dado de baja."
            )

        estado_disponible = (
            EstadoImplementoRepository()
            .obtener_por_codigo(
                db,
                "DISP",
            )
        )

        if estado_disponible is None:
            raise ValueError(
                "No existe el estado DISP."
            )

        if implemento.estado_id != estado_disponible.id:
            raise ValueError(
                "Solo pueden darse de baja implementos disponibles."
            )

        numero = cls._generar_numero(db)

        baja = Baja(
            numero=numero,
            implemento_id=implemento.id,
            estado_anterior_id=estado_anterior,
            tipo_baja=datos.tipo_baja,
            observaciones=datos.observaciones,
            valor_residual=datos.valor_residual,
            usuario_baja_id=usuario_id,
        )

        try:

            BajaRepository.crear(
                db,
                baja,
            )

            ImplementoRepository.actualizar_estado(
                db,
                implemento,
                estado_baja.id,
            )

            db.commit()

            db.refresh(baja)

            return baja

        except Exception:

            db.rollback()

            raise

    @staticmethod
    def eliminar(
        db: Session,
        baja: Baja,
    ) -> None:

        BajaRepository.eliminar(
            db,
            baja,
        )

    @classmethod
    def _generar_numero(
        cls,
        db: Session,
    ) -> str:

        ultima = BajaRepository.obtener_ultima(db)

        if ultima is None:
            return "BAJ-000001"

        ultimo = int(
            ultima.numero.split("-")[1]
        )

        return f"BAJ-{ultimo + 1:06d}"

    @classmethod
    def _validar_tipo_baja(
        cls,
        tipo: str,
    ) -> None:

        if tipo not in cls.TIPOS_BAJA:
            raise ValueError(
                "Tipo de baja inválido."
            )