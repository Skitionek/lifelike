"""Add effective annotation config table with BFS refresh function

Revision ID: 001_add_folder_annotation_config
Revises: 000000000000
Create Date: 2026-04-18 00:00:00.000000

The .annotations files are stored as regular Files rows (mime_type =
'vnd.lifelike.filesystem/annotations') whose content is JSON stored in
files_content.raw_file.  The effective annotation config for every file
and directory is held in the regular table file_effective_annotation_config
and updated incrementally via refresh_effective_annotation_subtree() using a
Breadth-First traversal of the folder tree whenever a .annotations file changes.
No new column on the files table is needed.
"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '001_add_folder_annotation_config'
down_revision = '000000000000'
branch_labels = None
depends_on = None


def upgrade():
    # 1. Helper function: deep-merge two annotation_configs JSONB sub-objects.
    #    Inner (layer) wins for all top-level keys; annotation_methods is also deep-merged.
    op.execute("""
CREATE OR REPLACE FUNCTION jsonb_merge_annotation_configs(base jsonb, layer jsonb)
RETURNS jsonb LANGUAGE sql IMMUTABLE AS $$
    SELECT CASE
        WHEN base IS NULL THEN COALESCE(layer, '{}'::jsonb)
        WHEN layer IS NULL THEN COALESCE(base, '{}'::jsonb)
        ELSE
            (COALESCE(base, '{}') || COALESCE(layer, '{}'))
            || CASE
                WHEN (COALESCE(base, '{}') ? 'annotation_methods')
                     AND (COALESCE(layer, '{}') ? 'annotation_methods')
                THEN jsonb_build_object(
                    'annotation_methods',
                    COALESCE(base->'annotation_methods', '{}')
                    || COALESCE(layer->'annotation_methods', '{}')
                )
                ELSE '{}'::jsonb
               END
    END
$$;
""")

    # 2. Aggregate: fold multiple annotation_configs objects outermost→innermost.
    op.execute("""
CREATE AGGREGATE jsonb_merge_annotation_configs_agg(jsonb) (
    SFUNC = jsonb_merge_annotation_configs,
    STYPE = jsonb
);
""")

    # 3. Table: effective annotation config per file / directory.
    #
    #    Rows are written by refresh_effective_annotation_subtree() which is called
    #    whenever a .annotations file is created or updated.  Both ordinary files
    #    and directories receive entries.  The fallback _get_from_chain() path in
    #    FolderAnnotationService handles files whose row has not yet been populated.
    op.execute("""
CREATE TABLE file_effective_annotation_config (
    file_id                        INTEGER PRIMARY KEY REFERENCES files(id) ON DELETE CASCADE,
    hash_id                        VARCHAR(36) NOT NULL,
    effective_annotation_configs   JSONB,
    effective_fallback_organism    JSONB,
    effective_custom_annotations   JSONB NOT NULL DEFAULT '[]',
    effective_excluded_annotations JSONB NOT NULL DEFAULT '[]'
)
""")
    op.execute("CREATE UNIQUE INDEX ON file_effective_annotation_config (hash_id)")

    # 4. BFS refresh stored procedure.
    #
    #    Upserts effective annotation configs for start_folder_id and every
    #    descendant file / directory in a single SQL call.  The computation is
    #    identical to the old materialized-view query but scoped to the subtree,
    #    making partial updates cheap.
    #
    #    inherit: false at ancestor depth D discards all configs from depths > D.
    op.execute("""
CREATE OR REPLACE FUNCTION refresh_effective_annotation_subtree(start_folder_id INTEGER)
RETURNS void LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO file_effective_annotation_config AS tgt
        (file_id, hash_id,
         effective_annotation_configs,
         effective_fallback_organism,
         effective_custom_annotations,
         effective_excluded_annotations)
    WITH RECURSIVE
    -- All files and folders in the subtree rooted at start_folder_id (inclusive).
    subtree(id, parent_id) AS (
        SELECT id, parent_id
        FROM   files
        WHERE  id = start_folder_id
          AND  deletion_date IS NULL
        UNION ALL
        SELECT f.id, f.parent_id
        FROM   files   f
        JOIN   subtree s ON f.parent_id = s.id
        WHERE  f.deletion_date IS NULL
    ),
    -- For each subtree member walk its ancestor folders to collect .annotations files.
    -- depth 0 = direct parent, depth 1 = grandparent, etc.
    file_ancestors AS (
        SELECT f.id        AS file_id,
               f.parent_id AS folder_id,
               0           AS depth
        FROM   subtree f
        WHERE  f.parent_id IS NOT NULL
        UNION ALL
        SELECT fa.file_id,
               p.parent_id AS folder_id,
               fa.depth + 1
        FROM   file_ancestors fa
        JOIN   files p ON p.id = fa.folder_id
        WHERE  p.deletion_date IS NULL
    ),
    -- Resolve .annotations content for each (file, ancestor_folder) pair.
    ancestor_configs AS (
        SELECT fa.file_id,
               fa.depth,
               convert_from(fc.raw_file, 'UTF8')::jsonb AS config
        FROM   file_ancestors fa
        JOIN   files anf
                   ON  anf.parent_id = fa.folder_id
                   AND anf.filename  = '.annotations'
                   AND anf.mime_type = 'vnd.lifelike.filesystem/annotations'
                   AND anf.deletion_date IS NULL
                   AND anf.content_id IS NOT NULL
        JOIN   files_content fc ON fc.id = anf.content_id
    ),
    -- Innermost (lowest depth) inherit=false resets the accumulation window.
    effective_window AS (
        SELECT file_id,
               MIN(CASE WHEN (config->>'inherit') = 'false' THEN depth END) AS start_depth
        FROM   ancestor_configs
        GROUP  BY file_id
    ),
    -- Only configs within the effective window are applied.
    active_configs AS (
        SELECT ac.file_id, ac.depth, ac.config
        FROM   ancestor_configs ac
        LEFT   JOIN effective_window ew ON ew.file_id = ac.file_id
        WHERE  ew.start_depth IS NULL OR ac.depth <= ew.start_depth
    )
    SELECT
        f.id    AS file_id,
        f.hash_id,
        -- annotation_configs: outermost first so innermost wins.
        (
            SELECT jsonb_merge_annotation_configs_agg(
                       ac2.config->'annotation_configs'
                       ORDER BY ac2.depth DESC)
            FROM   active_configs ac2
            WHERE  ac2.file_id = f.id
              AND  ac2.config ? 'annotation_configs'
        ) AS effective_annotation_configs,
        -- fallback_organism: innermost wins.
        (
            SELECT ac3.config->'fallback_organism'
            FROM   active_configs ac3
            WHERE  ac3.file_id = f.id
              AND  ac3.config ? 'fallback_organism'
            ORDER  BY ac3.depth ASC
            LIMIT  1
        ) AS effective_fallback_organism,
        -- include lists accumulated outer→inner.
        COALESCE(
            (
                SELECT jsonb_agg(elem ORDER BY ac4.depth DESC)
                FROM   active_configs ac4
                CROSS  JOIN LATERAL jsonb_array_elements(
                           COALESCE(ac4.config->'include', '[]'::jsonb)
                       ) AS elem
                WHERE  ac4.file_id = f.id
            ),
            '[]'::jsonb
        ) AS effective_custom_annotations,
        -- exclude lists accumulated outer→inner.
        COALESCE(
            (
                SELECT jsonb_agg(elem ORDER BY ac5.depth DESC)
                FROM   active_configs ac5
                CROSS  JOIN LATERAL jsonb_array_elements(
                           COALESCE(ac5.config->'exclude', '[]'::jsonb)
                       ) AS elem
                WHERE  ac5.file_id = f.id
            ),
            '[]'::jsonb
        ) AS effective_excluded_annotations
    FROM subtree f
    ON CONFLICT (file_id) DO UPDATE SET
        hash_id                        = EXCLUDED.hash_id,
        effective_annotation_configs   = EXCLUDED.effective_annotation_configs,
        effective_fallback_organism    = EXCLUDED.effective_fallback_organism,
        effective_custom_annotations   = EXCLUDED.effective_custom_annotations,
        effective_excluded_annotations = EXCLUDED.effective_excluded_annotations;
END;
$$;
""")


def downgrade():
    op.execute("DROP FUNCTION IF EXISTS refresh_effective_annotation_subtree(INTEGER)")
    op.execute("DROP TABLE IF EXISTS file_effective_annotation_config")
    op.execute("DROP AGGREGATE IF EXISTS jsonb_merge_annotation_configs_agg(jsonb)")
    op.execute("DROP FUNCTION IF EXISTS jsonb_merge_annotation_configs(jsonb, jsonb)")

