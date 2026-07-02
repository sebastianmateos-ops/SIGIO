from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)

    nombre: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    descripcion: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    implementos: Mapped[list["Implemento"]] = relationship(
        "Implemento",
        back_populates="categoria",
    )