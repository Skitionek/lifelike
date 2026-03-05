"""Add needs_reannotation column to files table

Revision ID: a1b2c3d4e5f6
Revises: cf9f210458c8
Create Date: 2026-03-05 22:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = 'cf9f210458c8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'files',
        sa.Column('needs_reannotation', sa.Boolean(), nullable=False, server_default='false')
    )


def downgrade():
    op.drop_column('files', 'needs_reannotation')
