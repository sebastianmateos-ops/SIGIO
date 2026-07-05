"""crear tabla bajas

Revision ID: d781e52eb17a
Revises: f16e21bff427
Create Date: 2026-07-05 14:44:48.101244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd781e52eb17a'
down_revision: Union[str, Sequence[str], None] = 'f16e21bff427'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "bajas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("numero", sa.String(length=20), nullable=False),

        sa.Column("implemento_id", sa.Integer(), nullable=False),
        sa.Column("estado_anterior_id", sa.Integer(), nullable=False),

        sa.Column("fecha", sa.DateTime(), nullable=False),

        sa.Column("tipo_baja", sa.String(length=30), nullable=False),

        sa.Column("observaciones", sa.String(length=500), nullable=True),

        sa.Column("valor_residual", sa.Numeric(12, 2), nullable=True),

        sa.Column("usuario_baja_id", sa.Integer(), nullable=False),

        sa.Column("activo", sa.Boolean(), nullable=False),

        sa.Column("fecha_creacion", sa.DateTime(), nullable=False),

        sa.Column("fecha_actualizacion", sa.DateTime(), nullable=True),

        sa.Column("usuario_responsable_id", sa.Integer(), nullable=True),

        sa.ForeignKeyConstraint(
            ["implemento_id"],
            ["implementos.id"],
        ),

        sa.ForeignKeyConstraint(
            ["estado_anterior_id"],
            ["estados_implemento.id"],
        ),

        sa.ForeignKeyConstraint(
            ["usuario_baja_id"],
            ["usuarios.id"],
        ),

        sa.ForeignKeyConstraint(
            ["usuario_responsable_id"],
            ["usuarios.id"],
        ),

        sa.PrimaryKeyConstraint("id"),

        sa.UniqueConstraint("uuid"),

        sa.UniqueConstraint("numero"),

        sa.UniqueConstraint("implemento_id"),
    )

    op.create_index(
        op.f("ix_bajas_numero"),
        "bajas",
        ["numero"],
        unique=True,
    )

    op.create_index(
        op.f("ix_bajas_activo"),
        "bajas",
        ["activo"],
        unique=False,
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_bajas_activo"),
        table_name="bajas",
    )

    op.drop_index(
        op.f("ix_bajas_numero"),
        table_name="bajas",
    )

    op.drop_table("bajas")