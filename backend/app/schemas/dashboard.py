from pydantic import BaseModel


class DashboardResumen(BaseModel):
    total_implementos: int
    disponibles: int
    prestados: int
    mantenimiento: int
    bajas: int


class DashboardBeneficiarios(BaseModel):
    activos: int


class DashboardPrestamos(BaseModel):
    activos: int
    finalizados: int


class DashboardMantenimientos(BaseModel):
    activos: int
    finalizados: int


class DashboardAdquisiciones(BaseModel):
    total: int


class DashboardBajas(BaseModel):
    total: int


class DashboardResponse(BaseModel):
    resumen: DashboardResumen
    beneficiarios: DashboardBeneficiarios
    prestamos: DashboardPrestamos
    mantenimientos: DashboardMantenimientos
    adquisiciones: DashboardAdquisiciones
    bajas: DashboardBajas