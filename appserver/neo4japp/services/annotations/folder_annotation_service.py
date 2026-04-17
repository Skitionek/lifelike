"""Folder-level annotation configuration service.

Reads `.annotations` YAML files from the ancestor folder chain of a given
file and merges them into a single :class:`EffectiveAnnotationConfig`.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import yaml

from neo4japp.constants import FILE_MIME_TYPE_ANNOTATIONS
from neo4japp.database import db
from neo4japp.models.files import Files

# Sentinel used to represent "no config file found" in the chain
_MISSING = object()

ANNOTATIONS_FILENAME = '.annotations'


@dataclass
class EffectiveAnnotationConfig:
    """Merged annotation configuration resolved from folder-level .annotations files
    combined with any per-file overrides.
    """
    annotation_configs: Optional[Dict[str, Any]] = None
    fallback_organism: Optional[Dict[str, str]] = None
    custom_annotations: List[dict] = field(default_factory=list)
    excluded_annotations: List[dict] = field(default_factory=list)


def _load_yaml(raw_bytes: bytes) -> dict:
    """Parse YAML bytes into a dict, returning {} on empty/invalid content."""
    try:
        data = yaml.safe_load(raw_bytes.decode('utf-8'))
        return data if isinstance(data, dict) else {}
    except (yaml.YAMLError, UnicodeDecodeError):
        return {}


def _lookup_annotations_file(folder_id: int) -> Optional[bytes]:
    """Return the raw content bytes of the .annotations file inside *folder_id*,
    or ``None`` if no such file exists.
    """
    row = (
        db.session.query(Files.id, Files.content_id)
        .filter(
            Files.filename == ANNOTATIONS_FILENAME,
            Files.parent_id == folder_id,
            Files.mime_type == FILE_MIME_TYPE_ANNOTATIONS,
            Files.deletion_date.is_(None),
        )
        .one_or_none()
    )
    if row is None:
        return None

    # Lazily load only the raw content without pulling in the full ORM object
    from neo4japp.models.files import FileContent
    content = (
        db.session.query(FileContent.raw_file)
        .filter(FileContent.id == row.content_id)
        .scalar()
    )
    return content


def _merge_layer(base: EffectiveAnnotationConfig, layer: dict) -> EffectiveAnnotationConfig:
    """Merge one .annotations layer on top of *base*.

    Rules:
    - ``annotation_configs`` is deep-merged (inner overrides outer per entity type).
    - ``fallback_organism`` replaces the outer value if present.
    - ``include`` / ``exclude`` lists are *accumulated* (inner appended after outer).
    """
    result = EffectiveAnnotationConfig(
        annotation_configs=dict(base.annotation_configs) if base.annotation_configs else None,
        fallback_organism=base.fallback_organism,
        custom_annotations=list(base.custom_annotations),
        excluded_annotations=list(base.excluded_annotations),
    )

    # fallback_organism
    if layer.get('fallback_organism'):
        result.fallback_organism = layer['fallback_organism']

    # annotation_configs
    layer_annotation_configs = layer.get('annotation_configs')
    if layer_annotation_configs:
        merged = dict(result.annotation_configs or {})
        layer_methods = layer_annotation_configs.get('annotation_methods', {})
        if layer_methods:
            existing_methods = dict(merged.get('annotation_methods', {}))
            existing_methods.update(layer_methods)
            merged['annotation_methods'] = existing_methods
        if 'exclude_references' in layer_annotation_configs:
            merged['exclude_references'] = layer_annotation_configs['exclude_references']
        result.annotation_configs = merged if merged else None

    # include / custom_annotations
    for inc in layer.get('include', []):
        result.custom_annotations.append(inc)

    # exclude / excluded_annotations
    for exc in layer.get('exclude', []):
        result.excluded_annotations.append(exc)

    return result


class FolderAnnotationService:
    """Resolves effective annotation configuration for a file by walking its
    ancestor folder chain and merging any `.annotations` YAML files found.
    """

    def get_effective_annotation_config(
        self,
        file: Files,
        *,
        per_file_custom_annotations: Optional[List[dict]] = None,
        per_file_excluded_annotations: Optional[List[dict]] = None,
        per_file_annotation_configs: Optional[Dict[str, Any]] = None,
        per_file_organism: Any = None,
    ) -> EffectiveAnnotationConfig:
        """Walk the ancestor chain of *file* and merge .annotations configs.

        The resolution order is: outermost folder → innermost folder → per-file.
        Any scope that sets ``inherit: false`` discards everything accumulated
        from outer scopes up to that point.

        :param file: the target file whose effective config should be resolved
        :param per_file_custom_annotations: per-file custom inclusions (backward compat)
        :param per_file_excluded_annotations: per-file exclusions (backward compat)
        :param per_file_annotation_configs: per-file annotation_configs (backward compat)
        :param per_file_organism: per-file FallbackOrganism (backward compat)
        :return: merged :class:`EffectiveAnnotationConfig`
        """
        # Build the ancestor folder path (root → parent of file).
        # file_path returns [root, …, file] so we skip the file itself and
        # iterate over just the folder portion.
        ancestors: List[Files] = []
        try:
            path = file.file_path  # [root, ..., file]
            ancestors = path[:-1]  # exclude the file itself
        except Exception:
            ancestors = []

        # Collect raw layers in order: outer → inner
        layers: List[dict] = []
        for ancestor in ancestors:
            raw = _lookup_annotations_file(ancestor.id)
            if raw is None:
                continue
            layer = _load_yaml(raw)
            if not layer:
                continue
            if not layer.get('inherit', True):
                # Reset — discard everything accumulated so far
                layers = []
            layers.append(layer)

        # Merge accumulated layers
        effective = EffectiveAnnotationConfig()
        for layer in layers:
            effective = _merge_layer(effective, layer)

        # Finally apply per-file overrides as the innermost layer
        per_file_layer: dict = {}
        if per_file_annotation_configs:
            per_file_layer['annotation_configs'] = per_file_annotation_configs
        if per_file_organism:
            per_file_layer['fallback_organism'] = {
                'synonym': per_file_organism.organism_synonym,
                'taxonomy_id': per_file_organism.organism_taxonomy_id,
            }
        if per_file_custom_annotations:
            per_file_layer['include'] = per_file_custom_annotations
        if per_file_excluded_annotations:
            per_file_layer['exclude'] = per_file_excluded_annotations

        if per_file_layer:
            effective = _merge_layer(effective, per_file_layer)

        return effective
