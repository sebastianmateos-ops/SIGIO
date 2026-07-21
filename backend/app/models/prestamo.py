from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.database import Base
from app.models.mixins import AuditMixin


class Prestamo(AuditMixin, Base):
    __tablename__ = "prestamos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )

    implemento_id: Mapped[int] = mapped_column(
        ForeignKey("implementos.id"),
        nullable=False,
        index=True,
    )

    beneficiario_id: Mapped[int] = mapped_column(
        ForeignKey("beneficiarios.id"),
        nullable=False,
        index=True,
    )

    fecha_prestamo: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    fecha_devolucion: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    observaciones: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    implemento: Mapped["Implemento"] = relationship(
        "Implemento",
        back_populates="prestamos",
    )

    beneficiario: Mapped["Beneficiario"] = relationship(
        "Beneficiario",
        back_populates="prestamos",
    )