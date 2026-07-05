from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.mixins import AuditMixin


class Baja(AuditMixin, Base):
    __tablename__ = "bajas"

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

    implemento_id: Mapped[int] = mapped_column(
        ForeignKey("implementos.id"),
        nullable=False,
        unique=True,
    )

    estado_anterior_id: Mapped[int] = mapped_column(
        ForeignKey("estados_implemento.id"),
        nullable=False,
    )

    fecha: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    tipo_baja: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    valor_residual: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    usuario_baja_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
    )

    implemento = relationship(
        "Implemento",
    )

    estado_anterior = relationship(
        "EstadoImplemento",
    )

    usuario_baja = relationship(
        "Usuario",
        foreign_keys=[usuario_baja_id],
    )