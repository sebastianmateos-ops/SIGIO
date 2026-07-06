from datetime import date

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# FILTROS
# ==========================================================

class ReporteFiltroBase(BaseModel):
    activo: bool | None = None


class ReporteInventarioFiltro(ReporteFiltroBase):

    categoria_id: int | None = Field(default=None, gt=0)

    estado_id: int | None = Field(default=None, gt=0)


class ReportePrestamoFiltro(ReporteFiltroBase):

    beneficiario_id: int | None = Field(default=None, gt=0)

    implemento_id: int | None = Field(default=None, gt=0)

    fecha_desde: date | None = None

    fecha_hasta: date | None = None


class ReporteMantenimientoFiltro(ReporteFiltroBase):

    implemento_id: int | None = Field(
        default=None,
        gt=0,
    )

    estado: str | None = None

    usuario_ingreso_id: int | None = Field(
        default=None,
        gt=0,
    )

    usuario_salida_id: int | None = Field(
        default=None,
        gt=0,
    )

    fecha_desde: date | None = None

    fecha_hasta: date | None = None


# ==========================================================
# INVENTARIO
# ==========================================================

class ReporteInventarioItem(BaseModel):

    codigo: str

    categoria: str

    estado: str

    marca: str | None

    modelo: str | None

    ubicacion: str | None

    activo: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


# ==========================================================
# PRESTAMOS
# ==========================================================

class ReportePrestamoItem(BaseModel):

    numero: str

    fecha_prestamo: date

    fecha_prevista_devolucion: date | None

    fecha_devolucion: date | None

    beneficiario: str

    documento: str

    implemento: str

    categoria: str

    activo: bool

    observaciones: str | None

    model_config = ConfigDict(
        from_attributes=True,
    )


# ==========================================================
# MANTENIMIENTOS
# ==========================================================

class ReporteMantenimientoItem(BaseModel):

    implemento: str

    categoria: str

    fecha_ingreso: date

    fecha_salida: date | None

    motivo: str

    estado: str

    usuario_ingreso: str

    usuario_salida: str | None

    observaciones: str | None

    model_config = ConfigDict(
        from_attributes=True,
    )