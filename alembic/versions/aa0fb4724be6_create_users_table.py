"""create account table

Revision ID: aa0fb4724be6
Revises: 
Create Date: 2021-04-07 11:25:50.708879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa0fb4724be6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(250), nullable=False),
        sa.Column('hashed_password', sa.String(250)),
        sa.Column('is_active', sa.Boolean()),
    )


def downgrade():
    op.drop_table('users')
