from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class PrestamoBase(BaseModel):
    beneficiario_id: int = Field(
        gt=0,
        description="ID del beneficiario.",
    )

    implemento_id: int = Field(
        gt=0,
        description="ID del implemento.",
    )

    fecha_prevista_devolucion: date | None = Field(
        default=None,
        description="Fecha prevista para la devolución.",
    )

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )


class PrestamoCreate(PrestamoBase):
    pass


class PrestamoUpdate(BaseModel):
    fecha_prevista_devolucion: date | None = None

    fecha_devolucion: datetime | None = None

    estado: str | None = None

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )

class PrestamoDevolucion(BaseModel):
    """
    Datos requeridos para registrar
    la devolución de un préstamo.
    """

    observaciones: str | None = Field(
        default=None,
        max_length=500,
        description="Observaciones de la devolución.",
    )

class PrestamoResponse(PrestamoBase):

    id: int

    uuid: str

    numero: str

    usuario_entrega_id: int

    usuario_devolucion_id: int | None

    fecha_prestamo: datetime

    fecha_devolucion: datetime | None

    estado: str

    activo: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class PrestamoListado(BaseModel):

    id: int

    numero: str

    beneficiario_id: int

    implemento_id: int

    fecha_prestamo: datetime

    fecha_prevista_devolucion: date | None

    estado: str

    model_config = ConfigDict(
        from_attributes=True,
    )