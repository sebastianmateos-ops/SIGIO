from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.beneficiario import Beneficiario


class BeneficiarioRepository:

    @staticmethod
    def listar(
        db: Session,
    ) -> list[Beneficiario]:

        return (
            db.query(Beneficiario)
            .filter(Beneficiario.activo.is_(True))
            .order_by(
                Beneficiario.apellido,
                Beneficiario.nombre,
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(
        db: Session,
        beneficiario_id: int,
    ) -> Beneficiario | None:

        return (
            db.query(Beneficiario)
            .filter(
                Beneficiario.id == beneficiario_id,
            )
            .first()
        )

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Beneficiario | None:

        return (
            db.query(Beneficiario)
            .filter(
                Beneficiario.uuid == uuid,
            )
            .first()
        )

    @staticmethod
    def obtener_por_documento(
        db: Session,
        tipo_documento: str,
        numero_documento: str,
    ) -> Beneficiario | None:

        return (
            db.query(Beneficiario)
            .filter(
                Beneficiario.tipo_documento == tipo_documento,
                Beneficiario.numero_documento == numero_documento,
            )
            .first()
        )

    @staticmethod
    def obtener_ultimo_codigo(
        db: Session,
    ) -> str | None:

        ultimo = (
            db.query(Beneficiario)
            .order_by(Beneficiario.codigo.desc())
            .first()
        )

        if ultimo:
            return ultimo.codigo

        return None

    @staticmethod
    def buscar(
        db: Session,
        texto: str,
    ) -> list[Beneficiario]:

        return (
            db.query(Beneficiario)
            .filter(
                Beneficiario.activo.is_(True),
                or_(
                    Beneficiario.codigo.ilike(f"%{texto}%"),
                    Beneficiario.nombre.ilike(f"%{texto}%"),
                    Beneficiario.apellido.ilike(f"%{texto}%"),
                    Beneficiario.numero_documento.ilike(f"%{texto}%"),
                ),
            )
            .order_by(
                Beneficiario.apellido,
                Beneficiario.nombre,
            )
            .all()
        )

    @staticmethod
    def crear(
        db: Session,
        beneficiario: Beneficiario,
    ) -> Beneficiario:

        db.add(beneficiario)
        db.commit()
        db.refresh(beneficiario)

        return beneficiario

    @staticmethod
    def actualizar(
        db: Session,
        beneficiario: Beneficiario,
    ) -> Beneficiario:

        db.commit()
        db.refresh(beneficiario)

        return beneficiario

    @staticmethod
    def eliminar(
        db: Session,
        beneficiario: Beneficiario,
    ) -> None:

        beneficiario.activo = False

        db.commit()
        db.refresh(beneficiario)