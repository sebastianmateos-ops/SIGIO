from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MantenimientoBase(BaseModel):

    implemento_id: int = Field(
        gt=0,
        description="ID del implemento.",
    )

    motivo: str = Field(
        min_length=3,
        max_length=200,
        description="Motivo del mantenimiento.",
    )

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )


class MantenimientoCreate(MantenimientoBase):
    pass


class MantenimientoSalida(BaseModel):

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )


class MantenimientoResponse(MantenimientoBase):

    id: int

    uuid: str

    usuario_ingreso_id: int

    usuario_salida_id: int | None

    fecha_ingreso: datetime

    fecha_salida: datetime | None

    estado: str

    activo: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class MantenimientoListado(BaseModel):

    id: int

    implemento_id: int

    fecha_ingreso: datetime

    fecha_salida: datetime | None

    motivo: str

    estado: str

    model_config = ConfigDict(
        from_attributes=True,
    )