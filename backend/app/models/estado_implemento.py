from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class EstadoImplemento(Base):
    __tablename__ = "estados_implemento"

    id: Mapped[int] = mapped_column(primary_key=True)

    codigo: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )

    nombre: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    descripcion: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    implementos: Mapped[list["Implemento"]] = relationship(
        "Implemento",
        back_populates="estado",
    )