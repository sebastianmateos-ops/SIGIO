"""mejorar tabla beneficiarios

Revision ID: aa55a178fa2d
Revises: d781e52eb17a
Create Date: 2026-07-12 03:40:29.611946

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aa55a178fa2d"
down_revision: Union[str, Sequence[str], None] = "d781e52eb17a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # -----------------------------------------------------------------
    # Agregar columnas nuevas
    # -----------------------------------------------------------------

    op.add_column(
        "beneficiarios",
        sa.Column(
            "codigo",
            sa.String(length=20),
            nullable=True,
        ),
    )

    op.add_column(
        "beneficiarios",
        sa.Column(
            "celular",
            sa.String(length=30),
            nullable=True,
        ),
    )

    # -----------------------------------------------------------------
    # Cambiar observaciones a TEXT
    # -----------------------------------------------------------------

    op.alter_column(
        "beneficiarios",
        "observaciones",
        existing_type=sa.String(length=500),
        type_=sa.Text(),
        existing_nullable=True,
    )

    # -----------------------------------------------------------------
    # Completar códigos existentes
    # -----------------------------------------------------------------

    connection = op.get_bind()

    metadata = sa.MetaData()

    beneficiarios = sa.Table(
        "beneficiarios",
        metadata,
        sa.Column("id", sa.Integer),
        sa.Column("codigo", sa.String(20)),
    )

    rows = connection.execute(
        sa.select(
            beneficiarios.c.id,
        ).order_by(
            beneficiarios.c.id,
        )
    ).fetchall()

    for numero, row in enumerate(rows, start=1):
        connection.execute(
            beneficiarios.update()
            .where(
                beneficiarios.c.id == row.id,
            )
            .values(
                codigo=f"BEN-{numero:06d}",
            )
        )

    # -----------------------------------------------------------------
    # Hacer código obligatorio
    # -----------------------------------------------------------------

    op.alter_column(
        "beneficiarios",
        "codigo",
        existing_type=sa.String(length=20),
        nullable=False,
    )

    # -----------------------------------------------------------------
    # Índice único
    # -----------------------------------------------------------------

    op.create_index(
        "ix_beneficiarios_codigo",
        "beneficiarios",
        ["codigo"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_beneficiarios_codigo",
        table_name="beneficiarios",
    )

    op.alter_column(
        "beneficiarios",
        "observaciones",
        existing_type=sa.Text(),
        type_=sa.String(length=500),
        existing_nullable=True,
    )

    op.drop_column(
        "beneficiarios",
        "celular",
    )

    op.drop_column(
        "beneficiarios",
        "codigo",
    )