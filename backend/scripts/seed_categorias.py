from app.db.database import SessionLocal
from app.models.categoria import Categoria


CATEGORIAS = [
    ("SR", "Silla de ruedas", "Sillas de ruedas manuales y eléctricas"),
    ("MU", "Muletas", "Muletas de aluminio o madera"),
    ("AN", "Andador", "Andadores para adultos"),
    ("BA", "Bastón", "Bastones simples y de cuatro apoyos"),
    ("CA", "Cama hospitalaria", "Camas articuladas"),
    ("CO", "Colchón antiescaras", "Colchones de prevención"),
]


def main():
    db = SessionLocal()

    try:
        for codigo, nombre, descripcion in CATEGORIAS:

            existe = (
                db.query(Categoria)
                .filter(Categoria.codigo == codigo)
                .first()
            )

            if existe:
                continue

            categoria = Categoria(
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
            )

            db.add(categoria)

        db.commit()

        print("✓ Categorías creadas correctamente")

    finally:
        db.close()


if __name__ == "__main__":
    main()