"""add foreign key to posts table

Revision ID: 29d6cfd470cf
Revises: 47e94778ba69
Create Date: 2026-10-05 15:02:53.320462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29d6cfd470cf'
down_revision: Union[str, Sequence[str], None] = '47e94778ba69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
