from datetime import UTC, datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class AuditMixin:
    """
    Campos comunes de auditoría para todas las entidades.
    """

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )

    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    fecha_actualizacion: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    usuario_responsable_id: Mapped[int | None] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=True,
    )