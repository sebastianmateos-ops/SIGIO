from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.mixins import AuditMixin


class Adquisicion(AuditMixin, Base):
    __tablename__ = "adquisiciones"

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

    fecha: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    tipo_origen: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    origen: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    telefono: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    usuario_registro_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
    )

    detalles: Mapped[list["AdquisicionImplemento"]] = relationship(
        "AdquisicionImplemento",
        back_populates="adquisicion",
        cascade="all, delete-orphan",
    )