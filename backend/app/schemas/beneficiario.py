from datetime import date, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)


class BeneficiarioBase(BaseModel):
    tipo_documento: str = Field(
        default="CI",
        max_length=20,
    )

    numero_documento: str = Field(
        ...,
        min_length=5,
        max_length=20,
    )

    nombre: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    apellido: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    fecha_nacimiento: date | None = None

    telefono: str | None = Field(
        default=None,
        max_length=30,
    )

    celular: str | None = Field(
        default=None,
        max_length=30,
    )

    email: EmailStr | None = None

    direccion: str | None = Field(
        default=None,
        max_length=255,
    )

    ciudad: str | None = Field(
        default=None,
        max_length=100,
    )

    departamento: str | None = Field(
        default=None,
        max_length=100,
    )

    observaciones: str | None = None

    activo: bool = True


class BeneficiarioCreate(BeneficiarioBase):
    pass


class BeneficiarioUpdate(BaseModel):
    tipo_documento: str | None = Field(
        default=None,
        max_length=20,
    )

    numero_documento: str | None = Field(
        default=None,
        min_length=5,
        max_length=20,
    )

    nombre: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    apellido: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    fecha_nacimiento: date | None = None

    telefono: str | None = Field(
        default=None,
        max_length=30,
    )

    celular: str | None = Field(
        default=None,
        max_length=30,
    )

    email: EmailStr | None = None

    direccion: str | None = Field(
        default=None,
        max_length=255,
    )

    ciudad: str | None = Field(
        default=None,
        max_length=100,
    )

    departamento: str | None = Field(
        default=None,
        max_length=100,
    )

    observaciones: str | None = None

    activo: bool | None = None


class BeneficiarioResponse(BeneficiarioBase):
    id: int
    uuid: str
    codigo: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime | None

    model_config = ConfigDict(
        from_attributes=True,
    )

class BeneficiarioSimple(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    codigo: str
    nombre: str
    apellido: str