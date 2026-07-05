"""agregar usuario_responsable a mantenimientos

Revision ID: 2a45af80c0c9
Revises: cbf03853d7df
Create Date: 2026-07-05

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a45af80c0c9"
down_revision: Union[str, Sequence[str], None] = "cbf03853d7df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "mantenimientos",
        sa.Column(
            "usuario_responsable_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_foreign_key(
        "fk_mantenimientos_usuario_responsable",
        "mantenimientos",
        "usuarios",
        ["usuario_responsable_id"],
        ["id"],
    )


def downgrade() -> None:

    op.drop_constraint(
        "fk_mantenimientos_usuario_responsable",
        "mantenimientos",
        type_="foreignkey",
    )

    op.drop_column(
        "mantenimientos",
        "usuario_responsable_id",
    )