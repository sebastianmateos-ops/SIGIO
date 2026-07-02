from app.db.database import SessionLocal
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.security.hash import hash_password


def main():
    db = SessionLocal()

    try:
        # Buscar rol Administrador
        rol = (
            db.query(Rol)
            .filter(Rol.nombre == "Administrador")
            .first()
        )

        if rol is None:
            rol = Rol(
                nombre="Administrador",
                descripcion="Administrador del sistema"
            )

            db.add(rol)
            db.commit()
            db.refresh(rol)

            print("✓ Rol Administrador creado")

        # Buscar usuario admin
        usuario = (
            db.query(Usuario)
            .filter(Usuario.usuario == "admin")
            .first()
        )

        if usuario is None:

            usuario = Usuario(
                nombre="Administrador",
                apellido="SIGIO",
                usuario="admin",
                email="admin@sigio.local",
                password_hash=hash_password("Admin123"),
                rol_id=rol.id,
                activo=True,
            )

            db.add(usuario)
            db.commit()

            print("✓ Usuario administrador creado")

        else:

            print("✓ El usuario admin ya existe")

    finally:
        db.close()


if __name__ == "__main__":
    main()