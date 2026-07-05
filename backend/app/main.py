from fastapi import FastAPI

from app.api.v1.auth import (
    router as auth_router,
)

from app.api.v1.implemento import (
    router as implemento_router,
)

from app.api.v1.beneficiario import (
    router as beneficiario_router,
)

from app.api.v1.prestamo import (
    router as prestamo_router,
)

from app.core.config import settings

from app.api.v1.mantenimiento import (
    router as mantenimiento_router,
)

app = FastAPI()

app.include_router(auth_router)
app.include_router(implemento_router)
app.include_router(beneficiario_router)
app.include_router(prestamo_router)
app.include_router(mantenimiento_router)


@app.get("/")
def root():
    return {
        "aplicacion": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "estado": "OK",
    }