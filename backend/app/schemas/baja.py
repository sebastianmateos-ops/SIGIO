from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class BajaBase(BaseModel):

    tipo_baja: str = Field(
        min_length=3,
        max_length=30,
    )

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )

    valor_residual: Decimal | None = Field(
        default=None,
        ge=0,
    )


class BajaCreate(BajaBase):

    implemento_id: int = Field(
        gt=0,
        description="ID del implemento.",
    )


class BajaResponse(BajaBase):

    id: int

    uuid: str

    numero: str

    implemento_id: int

    estado_anterior_id: int

    fecha: datetime

    usuario_baja_id: int

    activo: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class BajaListado(BaseModel):

    id: int

    numero: str

    implemento_id: int

    tipo_baja: str

    fecha: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )