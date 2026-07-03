"""insertar estados iniciales

Revision ID: a62dc3b902d1
Revises: 7a7777420e8a
Create Date: 2026-07-02 20:45:41.520903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a62dc3b902d1'
down_revision: Union[str, Sequence[str], None] = '7a7777420e8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        INSERT INTO estados_implemento (codigo, nombre, descripcion)
        VALUES
        ('DISP', 'Disponible', 'Implemento disponible para préstamo'),
        ('PRES', 'Prestado', 'Implemento entregado en préstamo'),
        ('MANT', 'Mantenimiento', 'Implemento en reparación o mantenimiento'),
        ('BAJA', 'Fuera de servicio', 'Implemento dado de baja');
    """)


def downgrade():
    op.execute("""
        DELETE FROM estados_implemento
        WHERE codigo IN ('DISP','PRES','MANT','BAJA');
    """)