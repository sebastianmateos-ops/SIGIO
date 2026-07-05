from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.mixins import AuditMixin


class Mantenimiento(AuditMixin, Base):
    __tablename__ = "mantenimientos"

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
    )

    usuario_ingreso_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
    )

    usuario_salida_id: Mapped[int | None] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=True,
    )

    fecha_ingreso: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    fecha_salida: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    motivo: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    estado: Mapped[str] = mapped_column(
        String(20),
        default="EN_MANTENIMIENTO",
        nullable=False,
    )

    implemento = relationship(
        "Implemento",
        back_populates="mantenimientos",
    )

    usuario_ingreso = relationship(
        "Usuario",
        foreign_keys=[usuario_ingreso_id],
    )

    usuario_salida = relationship(
        "Usuario",
        foreign_keys=[usuario_salida_id],
    )