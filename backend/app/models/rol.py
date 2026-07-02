from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Rol(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    descripcion: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    usuarios: Mapped[list["Usuario"]] = relationship(
        "Usuario",
        back_populates="rol",
    )