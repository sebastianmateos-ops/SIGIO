from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PrestamoBase(BaseModel):

    implemento_id: int = Field(
        gt=0,
    )

    beneficiario_id: int = Field(
        gt=0,
    )

    fecha_prestamo: datetime

    observaciones: str | None = Field(
        default=None,
        max_length=1000,
    )


class PrestamoCreate(PrestamoBase):
    pass


class PrestamoUpdate(BaseModel):

    fecha_devolucion: datetime | None = None

    observaciones: str | None = Field(
        default=None,
        max_length=1000,
    )


class PrestamoResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    uuid: str

    implemento_id: int

    beneficiario_id: int

    fecha_prestamo: datetime

    fecha_devolucion: datetime | None

    observaciones: str | None

    activo: bool


class PrestamoListResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    codigo_implemento: str

    implemento: str

    beneficiario: str

    fecha_prestamo: datetime

    fecha_devolucion: datetime | None

    activo: bool