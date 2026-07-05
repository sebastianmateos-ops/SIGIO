from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class AdquisicionImplementoCreate(BaseModel):
    implemento_id: int = Field(
        gt=0,
        description="ID del implemento.",
    )


class AdquisicionBase(BaseModel):

    tipo_origen: str = Field(
        min_length=3,
        max_length=30,
    )

    origen: str = Field(
        min_length=3,
        max_length=150,
    )

    telefono: str | None = Field(
        default=None,
        max_length=30,
    )

    email: EmailStr | None = None

    observaciones: str | None = Field(
        default=None,
        max_length=500,
    )


class AdquisicionCreate(AdquisicionBase):

    implementos: list[int] = Field(
        min_length=1,
        description="Lista de IDs de implementos.",
    )


class AdquisicionResponse(AdquisicionBase):

    id: int

    uuid: str

    numero: str

    fecha: datetime

    usuario_registro_id: int

    activo: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class AdquisicionListado(BaseModel):

    id: int

    numero: str

    fecha: datetime

    tipo_origen: str

    origen: str

    model_config = ConfigDict(
        from_attributes=True,
    )