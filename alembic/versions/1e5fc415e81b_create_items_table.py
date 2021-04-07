"""create item table

Revision ID: 1e5fc415e81b
Revises: aa0fb4724be6
Create Date: 2021-04-07 11:37:51.075052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e5fc415e81b'
down_revision = 'aa0fb4724be6'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(250), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    )

def downgrade():
    op.drop_table(
        'items'
    )
