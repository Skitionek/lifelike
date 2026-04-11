"""Squashed migration - initial schema from fresh DB

Revision ID: 000000000000
Revises:
Create Date: 2026-04-11 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '000000000000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # --- app_role ---
    op.create_table(
        'app_role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_app_role')),
        sa.UniqueConstraint('name', name=op.f('uq_app_role_name')),
    )

    # --- appuser ---
    op.create_table(
        'appuser',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=64), nullable=True),
        sa.Column('email', sa.String(length=120), nullable=True),
        sa.Column('first_name', sa.String(length=120), nullable=False),
        sa.Column('last_name', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=256), nullable=True),
        sa.Column('failed_login_count', sa.Integer(), server_default='0', nullable=True),
        sa.Column('forced_password_reset', sa.Boolean(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_appuser')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_appuser_hash_id')),
    )
    op.create_index(op.f('ix_appuser_email'), 'appuser', ['email'], unique=True)
    op.create_index(op.f('ix_appuser_username'), 'appuser', ['username'], unique=True)

    # --- app_user_role ---
    op.create_table(
        'app_user_role',
        sa.Column('appuser_id', sa.Integer(), nullable=False),
        sa.Column('app_role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['app_role_id'], ['app_role.id'],
            name=op.f('fk_app_user_role_app_role_id_app_role'), ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['appuser_id'], ['appuser.id'],
            name=op.f('fk_app_user_role_appuser_id_appuser'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('appuser_id', 'app_role_id', name=op.f('pk_app_user_role')),
    )
    op.create_index(op.f('ix_app_user_role_app_role_id'), 'app_user_role', ['app_role_id'], unique=False)
    op.create_index(op.f('ix_app_user_role_appuser_id'), 'app_user_role', ['appuser_id'], unique=False)

    # --- access_control_policy ---
    op.create_table(
        'access_control_policy',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('action', sa.Enum('READ', 'WRITE', name='accessactiontype'), nullable=False),
        sa.Column('asset_type', sa.String(length=200), nullable=False),
        sa.Column('asset_id', sa.Integer(), nullable=True),
        sa.Column('principal_type', sa.String(length=50), nullable=False),
        sa.Column('principal_id', sa.Integer(), nullable=True),
        sa.Column('rule_type', sa.Enum('ALLOW', 'DENY', name='accessruletype'), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_access_control_policy')),
    )
    op.create_index('ix_acp_asset_key', 'access_control_policy', ['asset_type', 'asset_id'], unique=False)
    op.create_index('ix_acp_principal_key', 'access_control_policy', ['principal_type', 'principal_id'], unique=False)

    # --- files_content ---
    op.create_table(
        'files_content',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('raw_file', sa.LargeBinary(), nullable=False),
        sa.Column('checksum_sha256', sa.LargeBinary(length=32), nullable=False),
        sa.Column('creation_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_files_content')),
    )
    op.create_index(
        op.f('ix_files_content_checksum_sha256'), 'files_content', ['checksum_sha256'], unique=True,
    )

    # --- fallback_organism ---
    op.create_table(
        'fallback_organism',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('organism_name', sa.String(length=200), nullable=False),
        sa.Column('organism_synonym', sa.String(length=200), nullable=False),
        sa.Column('organism_taxonomy_id', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_fallback_organism')),
    )

    # --- files ---
    op.create_table(
        'files',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('filename', sa.String(length=200), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.Column('mime_type', sa.String(length=127), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('content_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('doi', sa.String(length=1024), nullable=True),
        sa.Column('upload_url', sa.String(length=2048), nullable=True),
        sa.Column('public', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('deletion_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('recycling_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('annotations', postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=True),
        sa.Column('annotation_configs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('annotations_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('custom_annotations', postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=True),
        sa.Column('enrichment_annotations', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('excluded_annotations', postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=True),
        sa.Column('needs_reannotation', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('fallback_organism_id', sa.Integer(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('creator_id', sa.Integer(), nullable=True),
        sa.Column('modifier_id', sa.Integer(), nullable=True),
        sa.Column('deleter_id', sa.Integer(), nullable=True),
        sa.Column('recycler_id', sa.Integer(), nullable=True),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(
            ['content_id'], ['files_content.id'],
            name=op.f('fk_files_content_id_files_content'), ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['creator_id'], ['appuser.id'],
            name=op.f('fk_files_creator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['deleter_id'], ['appuser.id'],
            name=op.f('fk_files_deleter_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['fallback_organism_id'], ['fallback_organism.id'],
            name=op.f('fk_files_fallback_organism_id_fallback_organism'),
        ),
        sa.ForeignKeyConstraint(
            ['modifier_id'], ['appuser.id'],
            name=op.f('fk_files_modifier_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['parent_id'], ['files.id'],
            name=op.f('fk_files_parent_id_files'),
        ),
        sa.ForeignKeyConstraint(
            ['recycler_id'], ['appuser.id'],
            name=op.f('fk_files_recycler_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['appuser.id'],
            name=op.f('fk_files_user_id_appuser'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_files')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_files_hash_id')),
    )
    op.create_index(op.f('ix_files_content_id'), 'files', ['content_id'], unique=False)
    op.create_index(op.f('ix_files_fallback_organism_id'), 'files', ['fallback_organism_id'], unique=False)
    op.create_index(op.f('ix_files_parent_id'), 'files', ['parent_id'], unique=False)
    op.create_index(op.f('ix_files_user_id'), 'files', ['user_id'], unique=False)
    op.create_index(
        'uq_files_unique_filename',
        'files',
        ['filename', 'parent_id'],
        unique=True,
        postgresql_where=sa.text('deletion_date IS NULL AND recycling_date IS NULL AND parent_id IS NOT NULL'),
    )

    # --- file_collaborator_role ---
    op.create_table(
        'file_collaborator_role',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('collaborator_id', sa.Integer(), nullable=True),
        sa.Column('collaborator_email', sa.String(length=254), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('deletion_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('creator_id', sa.Integer(), nullable=True),
        sa.Column('modifier_id', sa.Integer(), nullable=True),
        sa.Column('deleter_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['collaborator_id'], ['appuser.id'],
            name=op.f('fk_file_collaborator_role_collaborator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['creator_id'], ['appuser.id'],
            name=op.f('fk_file_collaborator_role_creator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['deleter_id'], ['appuser.id'],
            name=op.f('fk_file_collaborator_role_deleter_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['file_id'], ['files.id'],
            name=op.f('fk_file_collaborator_role_file_id_files'),
        ),
        sa.ForeignKeyConstraint(
            ['modifier_id'], ['appuser.id'],
            name=op.f('fk_file_collaborator_role_modifier_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['owner_id'], ['appuser.id'],
            name=op.f('fk_file_collaborator_role_owner_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['role_id'], ['app_role.id'],
            name=op.f('fk_file_collaborator_role_role_id_app_role'),
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_file_collaborator_role')),
    )
    op.create_index(
        'uq_file_collaborator_role',
        'file_collaborator_role',
        ['file_id', 'collaborator_id', 'collaborator_email', 'role_id', 'owner_id'],
        unique=True,
        postgresql_where=sa.text('deletion_date IS NULL'),
    )
    op.create_index(
        op.f('ix_file_collaborator_role_collaborator_email'),
        'file_collaborator_role', ['collaborator_email'], unique=False,
    )
    op.create_index(
        op.f('ix_file_collaborator_role_collaborator_id'),
        'file_collaborator_role', ['collaborator_id'], unique=False,
    )
    op.create_index(
        op.f('ix_file_collaborator_role_file_id'),
        'file_collaborator_role', ['file_id'], unique=False,
    )
    op.create_index(
        op.f('ix_file_collaborator_role_role_id'),
        'file_collaborator_role', ['role_id'], unique=False,
    )

    # --- map_links ---
    op.create_table(
        'map_links',
        sa.Column('entry_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('map_id', sa.Integer(), nullable=False),
        sa.Column('linked_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['linked_id'], ['files.id'],
            name=op.f('fk_map_links_linked_id_files'),
        ),
        sa.ForeignKeyConstraint(
            ['map_id'], ['files.id'],
            name=op.f('fk_map_links_map_id_files'),
        ),
        sa.PrimaryKeyConstraint('entry_id', name=op.f('pk_map_links')),
    )

    # --- projects ---
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=250), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('root_id', sa.Integer(), nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('deletion_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('creator_id', sa.Integer(), nullable=True),
        sa.Column('modifier_id', sa.Integer(), nullable=True),
        sa.Column('deleter_id', sa.Integer(), nullable=True),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(
            ['creator_id'], ['appuser.id'],
            name=op.f('fk_projects_creator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['deleter_id'], ['appuser.id'],
            name=op.f('fk_projects_deleter_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['modifier_id'], ['appuser.id'],
            name=op.f('fk_projects_modifier_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['root_id'], ['files.id'],
            name=op.f('fk_projects_root_id_files'),
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_projects')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_projects_hash_id')),
        sa.UniqueConstraint('name', name=op.f('uq_projects_name')),
    )
    op.create_index(op.f('ix_projects_root_id'), 'projects', ['root_id'], unique=False)

    # --- projects_collaborator_role ---
    op.create_table(
        'projects_collaborator_role',
        sa.Column('appuser_id', sa.Integer(), nullable=False),
        sa.Column('app_role_id', sa.Integer(), nullable=False),
        sa.Column('projects_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['app_role_id'], ['app_role.id'],
            name=op.f('fk_projects_collaborator_role_app_role_id_app_role'), ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['appuser_id'], ['appuser.id'],
            name=op.f('fk_projects_collaborator_role_appuser_id_appuser'), ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['projects_id'], ['projects.id'],
            name=op.f('fk_projects_collaborator_role_projects_id_projects'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint(
            'appuser_id', 'app_role_id', 'projects_id',
            name=op.f('pk_projects_collaborator_role'),
        ),
    )
    op.create_index(
        op.f('ix_projects_collaborator_role_app_role_id'),
        'projects_collaborator_role', ['app_role_id'], unique=False,
    )
    op.create_index(
        op.f('ix_projects_collaborator_role_appuser_id'),
        'projects_collaborator_role', ['appuser_id'], unique=False,
    )
    op.create_index(
        op.f('ix_projects_collaborator_role_projects_id'),
        'projects_collaborator_role', ['projects_id'], unique=False,
    )

    # --- global_list ---
    op.create_table(
        'global_list',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('annotation', postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column('type', sa.String(length=12), nullable=False),
        sa.Column('file_content_id', sa.Integer(), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=True),
        sa.Column('reviewed', sa.Boolean(), nullable=True),
        sa.Column('approved', sa.Boolean(), nullable=True),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['file_content_id'], ['files_content.id'],
            name=op.f('fk_global_list_file_content_id_files_content'),
        ),
        sa.ForeignKeyConstraint(
            ['file_id'], ['files.id'],
            name=op.f('fk_global_list_file_id_files'),
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_global_list')),
    )
    op.create_index(op.f('ix_global_list_file_content_id'), 'global_list', ['file_content_id'], unique=False)
    op.create_index(op.f('ix_global_list_file_id'), 'global_list', ['file_id'], unique=False)

    # --- annotation_stop_words ---
    op.create_table(
        'annotation_stop_words',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('word', sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_annotation_stop_words')),
    )

    # --- lmdb ---
    op.create_table(
        'lmdb',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('checksum_md5', sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_lmdb')),
    )
    op.create_index(op.f('ix_lmdb_checksum_md5'), 'lmdb', ['checksum_md5'], unique=True)

    # --- domain_urls_map ---
    op.create_table(
        'domain_urls_map',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('domain', sa.String(length=128), nullable=False),
        sa.Column('base_URL', sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_domain_urls_map')),
    )

    # --- annotation_style ---
    op.create_table(
        'annotation_style',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('label', sa.String(length=32), nullable=False),
        sa.Column('color', sa.String(length=9), nullable=False),
        sa.Column('icon_code', sa.String(length=32), nullable=True),
        sa.Column('font_color', sa.String(length=9), nullable=True),
        sa.Column('border_color', sa.String(length=9), nullable=True),
        sa.Column('background_color', sa.String(length=9), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_annotation_style')),
    )

    # --- file_annotations_version ---
    op.create_table(
        'file_annotations_version',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column(
            'cause',
            sa.Enum('USER', 'USER_REANNOTATION', 'SYSTEM_REANNOTATION', name='annotationchangecause'),
            nullable=False,
        ),
        sa.Column(
            'custom_annotations',
            postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=True,
        ),
        sa.Column(
            'excluded_annotations',
            postgresql.JSONB(astext_type=sa.Text()), server_default='[]', nullable=True,
        ),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['file_id'], ['files.id'],
            name=op.f('fk_file_annotations_version_file_id_files'), ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['appuser.id'],
            name=op.f('fk_file_annotations_version_user_id_appuser'), ondelete='SET NULL',
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_file_annotations_version')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_file_annotations_version_hash_id')),
    )
    op.create_index(
        op.f('ix_file_annotations_version_file_id'),
        'file_annotations_version', ['file_id'], unique=False,
    )
    op.create_index(
        op.f('ix_file_annotations_version_user_id'),
        'file_annotations_version', ['user_id'], unique=False,
    )

    # --- file_version ---
    op.create_table(
        'file_version',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('deletion_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('creator_id', sa.Integer(), nullable=True),
        sa.Column('modifier_id', sa.Integer(), nullable=True),
        sa.Column('deleter_id', sa.Integer(), nullable=True),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.Column('message', sa.Text(), nullable=True),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('content_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['content_id'], ['files_content.id'],
            name=op.f('fk_file_version_content_id_files_content'),
        ),
        sa.ForeignKeyConstraint(
            ['creator_id'], ['appuser.id'],
            name=op.f('fk_file_version_creator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['deleter_id'], ['appuser.id'],
            name=op.f('fk_file_version_deleter_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['file_id'], ['files.id'],
            name=op.f('fk_file_version_file_id_files'),
        ),
        sa.ForeignKeyConstraint(
            ['modifier_id'], ['appuser.id'],
            name=op.f('fk_file_version_modifier_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['appuser.id'],
            name=op.f('fk_file_version_user_id_appuser'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_file_version')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_file_version_hash_id')),
    )
    op.create_index(op.f('ix_file_version_content_id'), 'file_version', ['content_id'], unique=False)
    op.create_index(op.f('ix_file_version_file_id'), 'file_version', ['file_id'], unique=False)
    op.create_index(op.f('ix_file_version_user_id'), 'file_version', ['user_id'], unique=False)

    # --- file_backup ---
    op.create_table(
        'file_backup',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('deletion_date', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('creator_id', sa.Integer(), nullable=True),
        sa.Column('modifier_id', sa.Integer(), nullable=True),
        sa.Column('deleter_id', sa.Integer(), nullable=True),
        sa.Column('hash_id', sa.String(length=36), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('raw_value', sa.LargeBinary(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['creator_id'], ['appuser.id'],
            name=op.f('fk_file_backup_creator_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['deleter_id'], ['appuser.id'],
            name=op.f('fk_file_backup_deleter_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['file_id'], ['files.id'],
            name=op.f('fk_file_backup_file_id_files'),
        ),
        sa.ForeignKeyConstraint(
            ['modifier_id'], ['appuser.id'],
            name=op.f('fk_file_backup_modifier_id_appuser'),
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['appuser.id'],
            name=op.f('fk_file_backup_user_id_appuser'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_file_backup')),
        sa.UniqueConstraint('hash_id', name=op.f('uq_file_backup_hash_id')),
    )
    op.create_index(op.f('ix_file_backup_file_id'), 'file_backup', ['file_id'], unique=False)
    op.create_index(op.f('ix_file_backup_user_id'), 'file_backup', ['user_id'], unique=False)

    # --- file_lock ---
    op.create_table(
        'file_lock',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('creation_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('modified_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('hash_id', sa.String(length=50), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('acquire_date', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'], ['appuser.id'],
            name=op.f('fk_file_lock_user_id_appuser'), ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_file_lock')),
    )
    op.create_index(op.f('ix_file_lock_hash_id'), 'file_lock', ['hash_id'], unique=True)
    op.create_index(op.f('ix_file_lock_user_id'), 'file_lock', ['user_id'], unique=False)

    # --- views ---
    op.create_table(
        'views',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('params', sa.JSON(), nullable=False),
        sa.Column('checksum_sha256', sa.LargeBinary(length=32), nullable=False),
        sa.Column('modification_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_views')),
    )
    op.create_index(op.f('ix_views_checksum_sha256'), 'views', ['checksum_sha256'], unique=True)


def downgrade():
    op.drop_table('views')
    op.drop_table('file_lock')
    op.drop_table('file_backup')
    op.drop_table('file_version')
    op.drop_table('file_annotations_version')
    op.drop_table('annotation_style')
    op.drop_table('domain_urls_map')
    op.drop_table('lmdb')
    op.drop_table('annotation_stop_words')
    op.drop_table('global_list')
    op.drop_table('projects_collaborator_role')
    op.drop_table('projects')
    op.drop_table('map_links')
    op.drop_table('file_collaborator_role')
    op.drop_table('files')
    op.drop_table('fallback_organism')
    op.drop_table('files_content')
    op.drop_table('access_control_policy')
    op.drop_table('app_user_role')
    op.drop_table('appuser')
    op.drop_table('app_role')
    sa.Enum(name='accessactiontype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='accessruletype').drop(op.get_bind(), checkfirst=True)
    sa.Enum(name='annotationchangecause').drop(op.get_bind(), checkfirst=True)
