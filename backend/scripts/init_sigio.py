from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.usuario import Usuario
from app.security.hash import hash_password


def crear_admin(db: Session):

    usuario = (
        db.query(Usuario)
        .filter(Usuario.usuario == "admin")
        .first()
    )

    if usuario:

        usuario.password_hash = hash_password("Admin1234")
        usuario.activo = True

        print("✓ Usuario admin actualizado.")

    else:

        usuario = Usuario(
            nombre="Administrador",
            apellido="SIGIO",
            usuario="admin",
            email="admin@sigio.local",
            password_hash=hash_password("Admin1234"),
            rol_id=1,
            activo=True,
        )

        db.add(usuario)

        print("✓ Usuario admin creado.")

    db.commit()


def main():

    db = SessionLocal()

    try:
        crear_admin(db)

    finally:
        db.close()


if __name__ == "__main__":
    main()