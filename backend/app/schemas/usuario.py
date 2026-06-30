from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    usuario: str
    email: EmailStr
    rol_id: int
    activo: bool = True


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    email: EmailStr | None = None
    rol_id: int | None = None
    activo: bool | None = None


class UsuarioResponse(UsuarioBase):
    id: int
    fecha_creacion: datetime
    ultimo_acceso: datetime | None

    model_config = ConfigDict(from_attributes=True)