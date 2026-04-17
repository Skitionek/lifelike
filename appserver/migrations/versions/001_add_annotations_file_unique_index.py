"""Add unique partial index for .annotations files per folder

Revision ID: 001_add_annotations_file_unique_index
Revises: 000000000000
Create Date: 2026-04-17 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001_add_annotations_file_unique_index'
down_revision = '000000000000'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(
        'uq_files_dot_annotations_per_folder',
        'files',
        ['filename', 'parent_id'],
        unique=True,
        postgresql_where=sa.text(
            "filename = '.annotations' AND deletion_date IS NULL"
        ),
    )


def downgrade():
    op.drop_index('uq_files_dot_annotations_per_folder', table_name='files')
