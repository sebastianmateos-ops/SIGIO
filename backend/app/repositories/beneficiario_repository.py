from sqlalchemy.orm import Session

from app.models.beneficiario import Beneficiario


class BeneficiarioRepository(BaseRepository[Beneficiario]):

    def __init__(self):
        super().__init__(Beneficiario)

    @staticmethod
    def obtener_por_uuid(
        db: Session,
        uuid: str,
    ) -> Beneficiario | None:

        return (
            db.query(Beneficiario)
            .filter(
                Beneficiario.uuid == uuid
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
    def buscar(
        db: Session,
        texto: str,
    ) -> list[Beneficiario]:

        return (
            db.query(Beneficiario)
            .filter(
                (Beneficiario.nombre.ilike(f"%{texto}%")) |
                (Beneficiario.apellido.ilike(f"%{texto}%")) |
                (Beneficiario.numero_documento.ilike(f"%{texto}%"))
            )
            .order_by(
                Beneficiario.apellido,
                Beneficiario.nombre,
            )
            .all()
        )