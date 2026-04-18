"""Add effective annotation config materialized view

Revision ID: 001_add_folder_annotation_config
Revises: 000000000000
Create Date: 2026-04-18 00:00:00.000000

The .annotations files are stored as regular Files rows (mime_type =
'vnd.lifelike.filesystem/annotations') whose content is normalised to JSON
by AnnotationsFileTypeProvider on upload.  The materialized view reads the
JSON directly from files_content.raw_file — no extra column on files is needed.
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

    # 3. Materialized view: effective annotation config per file.
    #
    #    For each non-deleted file the view precomputes the merged config from all
    #    .annotations files found in its ancestor folder chain (root → parent).
    #
    #    The .annotations file content is stored as UTF-8 JSON in files_content.raw_file
    #    (AnnotationsFileTypeProvider converts YAML→JSON on upload), so the view can
    #    read it with a plain cast — no extra column on the files table is needed.
    #
    #    inherit: false at folder depth D means all configs from folders further
    #    from the file (depth > D) are discarded; only configs from depth ≤ D onward
    #    are merged.
    op.execute("""
CREATE MATERIALIZED VIEW file_effective_annotation_config AS
WITH RECURSIVE file_ancestors AS (
    -- Base: each file starts from its direct parent folder (depth 0).
    SELECT
        f.id        AS file_id,
        f.parent_id AS folder_id,
        0           AS depth
    FROM files f
    WHERE f.deletion_date IS NULL
      AND f.parent_id IS NOT NULL

    UNION ALL

    -- Recursive: walk up the hierarchy.
    SELECT
        fa.file_id,
        p.parent_id AS folder_id,
        fa.depth + 1
    FROM file_ancestors fa
    JOIN files p ON p.id = fa.folder_id
    WHERE p.deletion_date IS NULL
),
-- For each (file, ancestor_folder) pair, find the .annotations config.
-- The raw_file bytes contain UTF-8 JSON (normalised by AnnotationsFileTypeProvider).
ancestor_configs AS (
    SELECT
        fa.file_id,
        fa.depth,
        convert_from(fc.raw_file, 'UTF8')::jsonb AS config
    FROM file_ancestors fa
    JOIN files anf
        ON  anf.parent_id = fa.folder_id
        AND anf.filename  = '.annotations'
        AND anf.mime_type = 'vnd.lifelike.filesystem/annotations'
        AND anf.deletion_date IS NULL
        AND anf.content_id IS NOT NULL
    JOIN files_content fc ON fc.id = anf.content_id
),
-- Determine the innermost (lowest depth) inherit=false reset point.
effective_window AS (
    SELECT
        file_id,
        MIN(CASE WHEN (config->>'inherit') = 'false' THEN depth END) AS start_depth
    FROM ancestor_configs
    GROUP BY file_id
),
-- Configs within the effective window.
active_configs AS (
    SELECT ac.file_id, ac.depth, ac.config
    FROM ancestor_configs ac
    LEFT JOIN effective_window ew ON ew.file_id = ac.file_id
    WHERE ew.start_depth IS NULL OR ac.depth <= ew.start_depth
)
SELECT
    f.id    AS file_id,
    f.hash_id,
    -- Merged annotation_configs: outermost first (ORDER BY depth DESC) so innermost wins.
    (
        SELECT jsonb_merge_annotation_configs_agg(ac2.config->'annotation_configs'
                                                  ORDER BY ac2.depth DESC)
        FROM active_configs ac2
        WHERE ac2.file_id = f.id
          AND ac2.config ? 'annotation_configs'
    ) AS effective_annotation_configs,
    -- Effective fallback_organism: innermost wins (lowest depth).
    (
        SELECT ac3.config->'fallback_organism'
        FROM active_configs ac3
        WHERE ac3.file_id = f.id
          AND ac3.config ? 'fallback_organism'
        ORDER BY ac3.depth ASC
        LIMIT 1
    ) AS effective_fallback_organism,
    -- Custom annotations (include lists): accumulated outer→inner.
    COALESCE(
        (
            SELECT jsonb_agg(elem ORDER BY ac4.depth DESC)
            FROM active_configs ac4
            CROSS JOIN LATERAL jsonb_array_elements(
                COALESCE(ac4.config->'include', '[]'::jsonb)
            ) AS elem
            WHERE ac4.file_id = f.id
        ),
        '[]'::jsonb
    ) AS effective_custom_annotations,
    -- Excluded annotations (exclude lists): accumulated outer→inner.
    COALESCE(
        (
            SELECT jsonb_agg(elem ORDER BY ac5.depth DESC)
            FROM active_configs ac5
            CROSS JOIN LATERAL jsonb_array_elements(
                COALESCE(ac5.config->'exclude', '[]'::jsonb)
            ) AS elem
            WHERE ac5.file_id = f.id
        ),
        '[]'::jsonb
    ) AS effective_excluded_annotations
FROM files f
WHERE f.deletion_date IS NULL
""")

    op.execute(
        "CREATE UNIQUE INDEX ON file_effective_annotation_config (file_id)"
    )
    op.execute(
        "CREATE UNIQUE INDEX ON file_effective_annotation_config (hash_id)"
    )


def downgrade():
    op.execute("DROP MATERIALIZED VIEW IF EXISTS file_effective_annotation_config")
    op.execute("DROP AGGREGATE IF EXISTS jsonb_merge_annotation_configs_agg(jsonb)")
    op.execute("DROP FUNCTION IF EXISTS jsonb_merge_annotation_configs(jsonb, jsonb)")

