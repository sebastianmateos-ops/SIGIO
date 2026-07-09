from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from pydantic import BaseModel, ConfigDict


class ImplementoBase(BaseModel):
    categoria_id: int
    marca: str | None = None
    modelo: str | None = None
    numero_serie: str | None = None
    valor_estimado: Decimal | None = None
    ubicacion: str | None = None
    observaciones: str | None = None


class ImplementoCreate(ImplementoBase):
    pass


class ImplementoUpdate(BaseModel):
    categoria_id: int | None = None
    marca: str | None = None
    modelo: str | None = None
    numero_serie: str | None = None
    valor_estimado: Decimal | None = None
    ubicacion: str | None = None
    observaciones: str | None = None
    activo: bool | None = None


class ImplementoResponse(ImplementoBase):
    id: int
    uuid: str
    codigo: str
    estado_id: int
    activo: bool
    fecha_ingreso: datetime

    model_config = ConfigDict(
    from_attributes=True,
    )


class ImplementoListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    codigo: str

    categoria: str

    marca: str | None = None
    modelo: str | None = None

    estado: str

    ubicacion: str | None = None