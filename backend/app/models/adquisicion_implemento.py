from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class AdquisicionImplemento(Base):
    __tablename__ = "adquisicion_implementos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    adquisicion_id: Mapped[int] = mapped_column(
        ForeignKey("adquisiciones.id"),
        nullable=False,
    )

    implemento_id: Mapped[int] = mapped_column(
        ForeignKey("implementos.id"),
        nullable=False,
    )

    adquisicion = relationship(
        "Adquisicion",
        back_populates="detalles",
    )

    implemento = relationship(
        "Implemento",
    )