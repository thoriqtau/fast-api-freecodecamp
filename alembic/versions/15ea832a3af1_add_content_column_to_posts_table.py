"""add content column to posts table

Revision ID: 15ea832a3af1
Revises: 247d091a9847
Create Date: 2025-08-03 21:18:43.374894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15ea832a3af1'
down_revision: Union[str, Sequence[str], None] = '247d091a9847'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
