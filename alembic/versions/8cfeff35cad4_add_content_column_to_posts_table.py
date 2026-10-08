"""add content column to posts table

Revision ID: 8cfeff35cad4
Revises: 26870f1ae29d
Create Date: 2026-10-03 17:36:01.115050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cfeff35cad4'
down_revision: Union[str, Sequence[str], None] = '26870f1ae29d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
