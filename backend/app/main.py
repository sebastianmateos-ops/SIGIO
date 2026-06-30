from fastapi import FastAPI

from app.core.config import settings
from app.db.database import Base, engine

# Registrar modelos
from app.models.usuario import Usuario

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "aplicacion": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "estado": "OK"
    }