from sqlalchemy.orm import Session

from app.models.adquisicion import Adquisicion
from app.models.adquisicion_implemento import AdquisicionImplemento
from app.repositories.adquisicion_implemento_repository import (
    AdquisicionImplementoRepository,
)
from app.repositories.adquisicion_repository import (
    AdquisicionRepository,
)
from app.repositories.implemento_repository import (
    ImplementoRepository,
)
from app.schemas.adquisicion import AdquisicionCreate


class AdquisicionService:

    TIPOS_ORIGEN = {
        "DONACION",
        "COMPRA",
        "TRANSFERENCIA",
        "CONVENIO",
        "RECUPERACION",
        "OTRO",
    }

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Adquisicion]:

        return AdquisicionRepository.listar(db)

    @staticmethod
    def obtener(
        db: Session,
        adquisicion_id: int,
    ) -> Adquisicion | None:

        return AdquisicionRepository.obtener_por_id(
            db,
            adquisicion_id,
        )

    @classmethod
    def crear(
        cls,
        db: Session,
        datos: AdquisicionCreate,
        usuario_id: int,
    ) -> Adquisicion:

        cls._validar_tipo_origen(
            datos.tipo_origen,
        )

        cls._validar_implementos(
            db,
            datos.implementos,
        )

        numero = cls._generar_numero(db)

        adquisicion = Adquisicion(
            numero=numero,
            tipo_origen=datos.tipo_origen,
            origen=datos.origen,
            telefono=datos.telefono,
            email=datos.email,
            observaciones=datos.observaciones,
            usuario_registro_id=usuario_id,
        )

        try:

            AdquisicionRepository.crear(
                db,
                adquisicion,
            )

            for implemento_id in datos.implementos:

                detalle = AdquisicionImplemento(
                    adquisicion_id=adquisicion.id,
                    implemento_id=implemento_id,
                )

                AdquisicionImplementoRepository.crear(
                    db,
                    detalle,
                )

            db.commit()

            db.refresh(adquisicion)

            return adquisicion

        except Exception:

            db.rollback()

            raise

    @staticmethod
    def eliminar(
        db: Session,
        adquisicion: Adquisicion,
    ) -> None:

        AdquisicionRepository.eliminar(
            db,
            adquisicion,
        )

    # -------------------------------------------------
    # Métodos privados
    # -------------------------------------------------

    @classmethod
    def _generar_numero(
        cls,
        db: Session,
    ) -> str:

        ultima = AdquisicionRepository.obtener_ultima(db)

        if ultima is None:

            return "ADQ-000001"

        ultimo = int(
            ultima.numero.split("-")[1]
        )

        return f"ADQ-{ultimo + 1:06d}"

    @classmethod
    def _validar_tipo_origen(
        cls,
        tipo: str,
    ) -> None:

        if tipo not in cls.TIPOS_ORIGEN:

            raise ValueError(
                "Tipo de origen inválido."
            )

    @staticmethod
    def _validar_implementos(
        db: Session,
        implementos: list[int],
    ) -> None:

        if len(implementos) != len(set(implementos)):

            raise ValueError(
                "Existen implementos repetidos."
            )

        for implemento_id in implementos:

            implemento = (
                ImplementoRepository.obtener_por_id(
                    db,
                    implemento_id,
                )
            )

            if implemento is None:

                raise ValueError(
                    f"Implemento {implemento_id} inexistente."
                )

            existe = (
                AdquisicionImplementoRepository.obtener_por_implemento(
                    db,
                    implemento_id,
                )
            )

            if existe is not None:

                raise ValueError(
                    f"El implemento {implemento.codigo} ya pertenece a una adquisición."
                )