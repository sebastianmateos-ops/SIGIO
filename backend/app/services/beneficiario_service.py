from sqlalchemy.orm import Session

from app.models.beneficiario import Beneficiario

from app.repositories.beneficiario_repository import (
    BeneficiarioRepository,
)

from app.schemas.beneficiario import (
    BeneficiarioCreate,
    BeneficiarioUpdate,
)


class BeneficiarioService:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Beneficiario]:

        return BeneficiarioRepository.listar(db)

    @staticmethod
    def obtener(
        db: Session,
        beneficiario_id: int,
    ) -> Beneficiario | None:

        return BeneficiarioService._obtener_beneficiario(
            db,
            beneficiario_id,
        )

    @staticmethod
    def buscar(
        db: Session,
        texto: str,
    ) -> list[Beneficiario]:

        return BeneficiarioRepository.buscar(
            db,
            texto,
        )

    @staticmethod
    def _obtener_beneficiario(
        db: Session,
        beneficiario_id: int,
    ) -> Beneficiario:

        beneficiario = (
            BeneficiarioRepository.obtener_por_id(
                db,
                beneficiario_id,
            )
        )

        if beneficiario is None:
            raise ValueError(
                "Beneficiario no encontrado."
            )

        return beneficiario

    @staticmethod
    def _validar_documento_unico(
        db: Session,
        tipo_documento: str,
        numero_documento: str,
        beneficiario_id: int | None = None,
    ) -> None:

        existente = (
            BeneficiarioRepository.obtener_por_documento(
                db,
                tipo_documento,
                numero_documento,
            )
        )

        if (
            existente is not None
            and existente.id != beneficiario_id
        ):
            raise ValueError(
                "Ya existe un beneficiario con ese documento."
            )

    @staticmethod
    def _generar_codigo(
        db: Session,
    ) -> str:

        ultimo = (
            BeneficiarioRepository.obtener_ultimo_codigo(
                db,
            )
        )

        if ultimo is None:
            return "BEN-000001"

        numero = int(
            ultimo.replace("BEN-", "")
        )

        return f"BEN-{numero + 1:06d}"

    @staticmethod
    def crear(
        db: Session,
        datos: BeneficiarioCreate,
    ) -> Beneficiario:

        BeneficiarioService._validar_documento_unico(
            db,
            datos.tipo_documento,
            datos.numero_documento,
        )

        codigo = (
            BeneficiarioService._generar_codigo(
                db,
            )
        )

        beneficiario = Beneficiario(
            codigo=codigo,
            tipo_documento=datos.tipo_documento,
            numero_documento=datos.numero_documento,
            nombre=datos.nombre,
            apellido=datos.apellido,
            fecha_nacimiento=datos.fecha_nacimiento,
            telefono=datos.telefono,
            celular=datos.celular,
            email=datos.email,
            direccion=datos.direccion,
            ciudad=datos.ciudad,
            departamento=datos.departamento,
            observaciones=datos.observaciones,
            activo=True,
        )

        return BeneficiarioRepository.crear(
            db,
            beneficiario,
        )

    @staticmethod
    def actualizar(
        db: Session,
        beneficiario_id: int,
        datos: BeneficiarioUpdate,
    ) -> Beneficiario:

        beneficiario = (
            BeneficiarioService._obtener_beneficiario(
                db,
                beneficiario_id,
            )
        )

        tipo_documento = (
            datos.tipo_documento
            if datos.tipo_documento is not None
            else beneficiario.tipo_documento
        )

        numero_documento = (
            datos.numero_documento
            if datos.numero_documento is not None
            else beneficiario.numero_documento
        )

        BeneficiarioService._validar_documento_unico(
            db,
            tipo_documento,
            numero_documento,
            beneficiario.id,
        )

        for campo, valor in (
            datos.model_dump(
                exclude_unset=True,
            ).items()
        ):
            setattr(
                beneficiario,
                campo,
                valor,
            )

        return BeneficiarioRepository.actualizar(
            db,
            beneficiario,
        )

    @staticmethod
    def eliminar(
        db: Session,
        beneficiario_id: int,
    ) -> None:

        beneficiario = (
            BeneficiarioService._obtener_beneficiario(
                db,
                beneficiario_id,
            )
        )

        BeneficiarioRepository.eliminar(
            db,
            beneficiario,
        )