from datetime import date
from uuid import uuid4

from sqlalchemy import (
    Date,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.database import Base
from app.models.mixins import AuditMixin


class Beneficiario(AuditMixin, Base):
    __tablename__ = "beneficiarios"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )

    tipo_documento: Mapped[str] = mapped_column(
        String(20),
        default="CI",
        nullable=False,
    )

    numero_documento: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    apellido: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    fecha_nacimiento: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    telefono: Mapped[str | None] = mapped_column(
        String(30),
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
    )

    direccion: Mapped[str | None] = mapped_column(
        String(255),
    )

    ciudad: Mapped[str | None] = mapped_column(
        String(100),
    )

    departamento: Mapped[str | None] = mapped_column(
        String(100),
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
    )

    prestamos: Mapped[list["Prestamo"]] = relationship(
        "Prestamo",
        back_populates="beneficiario",
    )