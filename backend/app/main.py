from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.adquisicion import router as adquisicion_router
from app.api.v1.auth import router as auth_router
from app.api.v1.baja import router as baja_router
from app.api.v1.beneficiario import router as beneficiario_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.implemento import router as implemento_router
from app.api.v1.mantenimiento import router as mantenimiento_router
from app.api.v1.prestamo import router as prestamo_router
from app.api.v1.reporte import router as reporte_router
from app.core.config import settings
from app.api.v1.categoria import router as categoria_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Sistema Integral de Gestión de Implementos Ortopédicos",
)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# API v1
# ==========================================================

API_PREFIX = "/api/v1"

app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(implemento_router, prefix=API_PREFIX)
app.include_router(beneficiario_router, prefix=API_PREFIX)
app.include_router(prestamo_router, prefix=API_PREFIX)
app.include_router(mantenimiento_router, prefix=API_PREFIX)
app.include_router(adquisicion_router, prefix=API_PREFIX)
app.include_router(baja_router, prefix=API_PREFIX)
app.include_router(dashboard_router, prefix=API_PREFIX)
app.include_router(reporte_router, prefix=API_PREFIX)
app.include_router(
    categoria_router,
    prefix=API_PREFIX,
)


@app.get(
    "/",
    tags=["Sistema"],
    summary="Estado del sistema",
)
def root():
    return {
        "aplicacion": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "estado": "OK",
    }
