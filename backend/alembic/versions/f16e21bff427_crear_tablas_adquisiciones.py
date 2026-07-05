"""crear tablas adquisiciones

Revision ID: f16e21bff427
Revises: 2a45af80c0c9
Create Date: 2026-07-05

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f16e21bff427"
down_revision: Union[str, Sequence[str], None] = "2a45af80c0c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "adquisiciones",

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
            "numero",
            sa.String(length=20),
            nullable=False,
            unique=True,
        ),

        sa.Column(
            "fecha",
            sa.DateTime(),
            nullable=False,
        ),

        sa.Column(
            "tipo_origen",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "origen",
            sa.String(length=150),
            nullable=False,
        ),

        sa.Column(
            "telefono",
            sa.String(length=30),
            nullable=True,
        ),

        sa.Column(
            "email",
            sa.String(length=150),
            nullable=True,
        ),

        sa.Column(
            "observaciones",
            sa.String(length=500),
            nullable=True,
        ),

        sa.Column(
            "usuario_registro_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id"),
            nullable=False,
        ),

        # AuditMixin
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

        sa.Column(
            "usuario_responsable_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id"),
            nullable=True,
        ),
    )

    op.create_index(
        "ix_adquisiciones_uuid",
        "adquisiciones",
        ["uuid"],
        unique=True,
    )

    op.create_index(
        "ix_adquisiciones_numero",
        "adquisiciones",
        ["numero"],
        unique=True,
    )

    op.create_index(
        "ix_adquisiciones_activo",
        "adquisiciones",
        ["activo"],
    )

    op.create_table(
        "adquisicion_implementos",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),

        sa.Column(
            "adquisicion_id",
            sa.Integer(),
            sa.ForeignKey(
                "adquisiciones.id",
                ondelete="CASCADE",
            ),
            nullable=False,
        ),

        sa.Column(
            "implemento_id",
            sa.Integer(),
            sa.ForeignKey("implementos.id"),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_adquisicion_implementos_adquisicion",
        "adquisicion_implementos",
        ["adquisicion_id"],
    )

    op.create_index(
        "ix_adquisicion_implementos_implemento",
        "adquisicion_implementos",
        ["implemento_id"],
    )


def downgrade() -> None:

    op.drop_index(
        "ix_adquisicion_implementos_implemento",
        table_name="adquisicion_implementos",
    )

    op.drop_index(
        "ix_adquisicion_implementos_adquisicion",
        table_name="adquisicion_implementos",
    )

    op.drop_table("adquisicion_implementos")

    op.drop_index(
        "ix_adquisiciones_activo",
        table_name="adquisiciones",
    )

    op.drop_index(
        "ix_adquisiciones_numero",
        table_name="adquisiciones",
    )

    op.drop_index(
        "ix_adquisiciones_uuid",
        table_name="adquisiciones",
    )

    op.drop_table("adquisiciones")