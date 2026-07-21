"""sincronizar prestamos con modelo

Revision ID: 5a01e3afd908
Revises: aa55a178fa2d
Create Date: 2026-07-21 01:24:15.449011

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5a01e3afd908"
down_revision: Union[str, Sequence[str], None] = "aa55a178fa2d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "prestamos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.String(length=36), nullable=False),
        sa.Column("implemento_id", sa.Integer(), nullable=False),
        sa.Column("beneficiario_id", sa.Integer(), nullable=False),
        sa.Column("fecha_prestamo", sa.DateTime(), nullable=False),
        sa.Column("fecha_devolucion", sa.DateTime(), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
        sa.Column("activo", sa.Boolean(), nullable=False),
        sa.Column("fecha_creacion", sa.DateTime(), nullable=False),
        sa.Column("fecha_actualizacion", sa.DateTime(), nullable=True),
        sa.Column("usuario_responsable_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["beneficiario_id"],
            ["beneficiarios.id"],
        ),
        sa.ForeignKeyConstraint(
            ["implemento_id"],
            ["implementos.id"],
        ),
        sa.ForeignKeyConstraint(
            ["usuario_responsable_id"],
            ["usuarios.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("uuid"),
    )

    op.create_index(
        op.f("ix_prestamos_beneficiario_id"),
        "prestamos",
        ["beneficiario_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_prestamos_implemento_id"),
        "prestamos",
        ["implemento_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_prestamos_implemento_id"),
        table_name="prestamos",
    )

    op.drop_index(
        op.f("ix_prestamos_beneficiario_id"),
        table_name="prestamos",
    )

    op.drop_table("prestamos")