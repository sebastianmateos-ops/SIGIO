from datetime import UTC, datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Implemento(Base):
    __tablename__ = "implementos"

    id: Mapped[int] = mapped_column(primary_key=True)

    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )

    codigo: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
        nullable=False,
    )

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id"),
        nullable=False,
    )

    estado_id: Mapped[int] = mapped_column(
        ForeignKey("estados_implemento.id"),
        nullable=False,
    )

    marca: Mapped[str | None] = mapped_column(String(100))

    modelo: Mapped[str | None] = mapped_column(String(100))

    numero_serie: Mapped[str | None] = mapped_column(String(100))

    valor_estimado: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
    )

    ubicacion: Mapped[str | None] = mapped_column(
        String(100),
    )

    observaciones: Mapped[str | None] = mapped_column(
        String(500),
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    fecha_ingreso: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
    )

    categoria: Mapped["Categoria"] = relationship(
        "Categoria",
        back_populates="implementos",
    )
    
    estado: Mapped["EstadoImplemento"] = relationship(
        "EstadoImplemento",
        back_populates="implementos",
    )