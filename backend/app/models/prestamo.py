from datetime import UTC, date, datetime
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    numero: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    beneficiario_id: Mapped[int] = mapped_column(
        ForeignKey("beneficiarios.id"),
        nullable=False,
    )

    implemento_id: Mapped[int] = mapped_column(
        ForeignKey("implementos.id"),
        nullable=False,
    )

    usuario_entrega_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
    )

    usuario_devolucion_id: Mapped[int | None] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=True,
    )

    fecha_prestamo: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    fecha_prevista_devolucion: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    fecha_devolucion: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    estado: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVO",
        nullable=False,
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    beneficiario: Mapped["Beneficiario"] = relationship(
        "Beneficiario",
        back_populates="prestamos",
    )

    implemento: Mapped["Implemento"] = relationship(
        "Implemento",
    )

    usuario_entrega: Mapped["Usuario"] = relationship(
        "Usuario",
        foreign_keys=[usuario_entrega_id],
    )

    usuario_devolucion: Mapped["Usuario | None"] = relationship(
        "Usuario",
        foreign_keys=[usuario_devolucion_id],
    )