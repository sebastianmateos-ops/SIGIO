from datetime import datetime, UTC

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    apellido: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    usuario: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    rol_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False
    )

    rol: Mapped["Rol"] = relationship(
        "Rol",
        back_populates="usuarios"
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC)
)

    ultimo_acceso: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )