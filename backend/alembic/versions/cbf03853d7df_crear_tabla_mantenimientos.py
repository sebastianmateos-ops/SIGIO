"""crear tabla mantenimientos

Revision ID: cbf03853d7df
Revises: 95f38a9c2fca
Create Date: 2026-07-05

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cbf03853d7df"
down_revision: Union[str, Sequence[str], None] = "95f38a9c2fca"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "mantenimientos",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),

        sa.Column(
            "uuid",
            sa.String(length=36),
            nullable=False,
            unique=True,
        ),

        sa.Column(
            "implemento_id",
            sa.Integer(),
            sa.ForeignKey("implementos.id"),
            nullable=False,
        ),

        sa.Column(
            "usuario_ingreso_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id"),
            nullable=False,
        ),

        sa.Column(
            "usuario_salida_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id"),
            nullable=True,
        ),

        sa.Column(
            "fecha_ingreso",
            sa.DateTime(),
            nullable=False,
        ),

        sa.Column(
            "fecha_salida",
            sa.DateTime(),
            nullable=True,
        ),

        sa.Column(
            "motivo",
            sa.String(length=200),
            nullable=False,
        ),

        sa.Column(
            "observaciones",
            sa.String(length=500),
            nullable=True,
        ),

        sa.Column(
            "estado",
            sa.String(length=20),
            nullable=False,
        ),

        sa.Column(
            "activo",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),

        sa.Column(
            "fecha_creacion",
            sa.DateTime(),
            nullable=False,
        ),

        sa.Column(
            "fecha_actualizacion",
            sa.DateTime(),
            nullable=True,
        ),
    )

    op.create_index(
        "ix_mantenimientos_uuid",
        "mantenimientos",
        ["uuid"],
        unique=True,
    )

    op.create_index(
        "ix_mantenimientos_implemento",
        "mantenimientos",
        ["implemento_id"],
    )

    op.create_index(
        "ix_mantenimientos_estado",
        "mantenimientos",
        ["estado"],
    )


def downgrade() -> None:

    op.drop_index(
        "ix_mantenimientos_estado",
        table_name="mantenimientos",
    )

    op.drop_index(
        "ix_mantenimientos_implemento",
        table_name="mantenimientos",
    )

    op.drop_index(
        "ix_mantenimientos_uuid",
        table_name="mantenimientos",
    )

    op.drop_table("mantenimientos")