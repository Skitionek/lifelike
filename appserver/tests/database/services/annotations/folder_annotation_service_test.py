"""Unit tests for FolderAnnotationService.

These tests are pure-unit tests that do NOT require a running database.
We monkey-patch the internal DB lookup function so the service can be
exercised in isolation.
"""
import yaml

from neo4japp.services.annotations.folder_annotation_service import (
    EffectiveAnnotationConfig,
    FolderAnnotationService,
    _load_yaml,
    _merge_layer,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_file(file_id, parent_id=None, annotations=None, custom_annotations=None,
               excluded_annotations=None, annotation_configs=None, fallback_organism=None):
    """Return a minimal Files-like object for use in tests."""

    class FakeOrganism:
        def __init__(self, synonym, taxonomy_id):
            self.organism_synonym = synonym
            self.organism_taxonomy_id = taxonomy_id

    class FakeFile:
        def __init__(self):
            self.id = file_id
            self.parent_id = parent_id
            self.annotations = annotations or []
            self.custom_annotations = custom_annotations or []
            self.excluded_annotations = excluded_annotations or []
            self.annotation_configs = annotation_configs
            self.fallback_organism = (
                FakeOrganism(*fallback_organism) if fallback_organism else None
            )
            # file_path property: just [self] unless overridden externally
            self._path = [self]

        @property
        def file_path(self):
            return self._path

    return FakeFile()


def _yaml_bytes(data: dict) -> bytes:
    return yaml.dump(data, allow_unicode=True).encode('utf-8')


# ---------------------------------------------------------------------------
# _load_yaml
# ---------------------------------------------------------------------------

class TestLoadYaml:
    def test_valid_yaml(self):
        raw = _yaml_bytes({'inherit': True, 'exclude': [{'type': 'Gene', 'text': 'foo'}]})
        result = _load_yaml(raw)
        assert result['inherit'] is True
        assert result['exclude'][0]['type'] == 'Gene'

    def test_empty_bytes(self):
        assert _load_yaml(b'') == {}

    def test_yaml_is_not_a_dict(self):
        assert _load_yaml(b'- item1\n- item2\n') == {}

    def test_invalid_utf8(self):
        assert _load_yaml(b'\xff\xfe') == {}


# ---------------------------------------------------------------------------
# _merge_layer
# ---------------------------------------------------------------------------

class TestMergeLayer:
    def test_fallback_organism_overrides(self):
        base = EffectiveAnnotationConfig(
            fallback_organism={'synonym': 'Outer', 'taxonomy_id': '1'}
        )
        layer = {'fallback_organism': {'synonym': 'Inner', 'taxonomy_id': '2'}}
        result = _merge_layer(base, layer)
        assert result.fallback_organism == {'synonym': 'Inner', 'taxonomy_id': '2'}

    def test_annotation_configs_deep_merged(self):
        base = EffectiveAnnotationConfig(
            annotation_configs={
                'exclude_references': True,
                'annotation_methods': {'Gene': {'nlp': False, 'rules_based': True}},
            }
        )
        layer = {
            'annotation_configs': {
                'annotation_methods': {'Disease': {'nlp': True, 'rules_based': False}}
            }
        }
        result = _merge_layer(base, layer)
        methods = result.annotation_configs['annotation_methods']
        assert 'Gene' in methods
        assert 'Disease' in methods
        assert result.annotation_configs['exclude_references'] is True

    def test_include_lists_accumulated(self):
        inc1 = {'type': 'Gene', 'text': 'TP53', 'id': '7157', 'isCaseInsensitive': False}
        inc2 = {'type': 'Chemical', 'text': 'aspirin', 'id': '', 'isCaseInsensitive': True}
        base = EffectiveAnnotationConfig(custom_annotations=[inc1])
        layer = {'include': [inc2]}
        result = _merge_layer(base, layer)
        assert len(result.custom_annotations) == 2

    def test_exclude_lists_accumulated(self):
        exc1 = {'type': 'Disease', 'text': 'cancer', 'isCaseInsensitive': True}
        exc2 = {'type': 'Gene', 'text': 'BRCA', 'isCaseInsensitive': False}
        base = EffectiveAnnotationConfig(excluded_annotations=[exc1])
        layer = {'exclude': [exc2]}
        result = _merge_layer(base, layer)
        assert len(result.excluded_annotations) == 2

    def test_empty_layer_preserves_base(self):
        base = EffectiveAnnotationConfig(
            fallback_organism={'synonym': 'E.coli', 'taxonomy_id': '511145'},
            annotation_configs={'exclude_references': False, 'annotation_methods': {}},
        )
        result = _merge_layer(base, {})
        assert result.fallback_organism == base.fallback_organism
        assert result.annotation_configs == base.annotation_configs


# ---------------------------------------------------------------------------
# FolderAnnotationService.get_effective_annotation_config
# ---------------------------------------------------------------------------

class TestFolderAnnotationService:
    """Tests that use monkeypatching to avoid a real DB."""

    def _build_service_with_layers(self, monkeypatch, folder_layers: dict):
        """
        :param folder_layers: {folder_id: yaml_bytes_or_None}
        """
        import neo4japp.services.annotations.folder_annotation_service as svc_mod

        def fake_lookup(folder_id):
            return folder_layers.get(folder_id)

        monkeypatch.setattr(svc_mod, '_lookup_annotations_file', fake_lookup)
        return FolderAnnotationService()

    def test_no_annotations_files(self, monkeypatch):
        """Returns empty config when no .annotations files exist."""
        root = _make_file(1)
        folder = _make_file(2, parent_id=1)
        leaf = _make_file(3, parent_id=2)
        leaf._path = [root, folder, leaf]

        svc = self._build_service_with_layers(monkeypatch, {})
        result = svc.get_effective_annotation_config(leaf)
        assert result.annotation_configs is None
        assert result.fallback_organism is None
        assert result.custom_annotations == []
        assert result.excluded_annotations == []

    def test_single_folder_config(self, monkeypatch):
        """Single .annotations file at root is applied."""
        root = _make_file(1)
        leaf = _make_file(2, parent_id=1)
        leaf._path = [root, leaf]

        layer_data = {
            'fallback_organism': {'synonym': 'E.coli', 'taxonomy_id': '511145'},
            'exclude': [{'type': 'Disease', 'text': 'cancer', 'isCaseInsensitive': True}],
        }
        svc = self._build_service_with_layers(
            monkeypatch, {root.id: _yaml_bytes(layer_data)}
        )
        result = svc.get_effective_annotation_config(leaf)
        assert result.fallback_organism['synonym'] == 'E.coli'
        assert len(result.excluded_annotations) == 1
        assert result.excluded_annotations[0]['text'] == 'cancer'

    def test_nested_configs_merged(self, monkeypatch):
        """Inner folder's config is merged on top of outer folder's config."""
        root = _make_file(1)
        inner = _make_file(2, parent_id=1)
        leaf = _make_file(3, parent_id=2)
        leaf._path = [root, inner, leaf]

        outer_data = {
            'fallback_organism': {'synonym': 'Outer', 'taxonomy_id': '1'},
            'annotation_configs': {
                'exclude_references': True,
                'annotation_methods': {'Gene': {'nlp': False, 'rules_based': True}},
            },
        }
        inner_data = {
            'fallback_organism': {'synonym': 'Inner', 'taxonomy_id': '2'},
            'annotation_configs': {
                'annotation_methods': {'Disease': {'nlp': True, 'rules_based': False}},
            },
        }
        svc = self._build_service_with_layers(
            monkeypatch,
            {root.id: _yaml_bytes(outer_data), inner.id: _yaml_bytes(inner_data)},
        )
        result = svc.get_effective_annotation_config(leaf)
        # Inner organism overrides outer
        assert result.fallback_organism['synonym'] == 'Inner'
        # Both entity method configs present
        methods = result.annotation_configs['annotation_methods']
        assert 'Gene' in methods
        assert 'Disease' in methods
        # exclude_references from outer is preserved
        assert result.annotation_configs['exclude_references'] is True

    def test_inherit_false_resets_stack(self, monkeypatch):
        """A scope with inherit=false discards all outer configs."""
        root = _make_file(1)
        inner = _make_file(2, parent_id=1)
        leaf = _make_file(3, parent_id=2)
        leaf._path = [root, inner, leaf]

        outer_data = {
            'fallback_organism': {'synonym': 'Outer', 'taxonomy_id': '1'},
            'exclude': [{'type': 'Gene', 'text': 'BRCA', 'isCaseInsensitive': False}],
        }
        inner_data = {
            'inherit': False,
            'fallback_organism': {'synonym': 'Inner', 'taxonomy_id': '2'},
        }
        svc = self._build_service_with_layers(
            monkeypatch,
            {root.id: _yaml_bytes(outer_data), inner.id: _yaml_bytes(inner_data)},
        )
        result = svc.get_effective_annotation_config(leaf)
        # inherit=False in inner resets outer config; only inner's config remains
        assert result.fallback_organism['synonym'] == 'Inner'
        assert result.excluded_annotations == []

    def test_per_file_overrides_applied_last(self, monkeypatch):
        """Per-file values are the innermost layer and override folder configs."""
        root = _make_file(1)
        leaf = _make_file(2, parent_id=1)
        leaf._path = [root, leaf]

        folder_data = {
            'fallback_organism': {'synonym': 'Folder', 'taxonomy_id': '10'},
        }
        svc = self._build_service_with_layers(
            monkeypatch, {root.id: _yaml_bytes(folder_data)}
        )

        class FakeOrg:
            organism_synonym = 'PerFile'
            organism_taxonomy_id = '99'

        result = svc.get_effective_annotation_config(
            leaf,
            per_file_organism=FakeOrg(),
        )
        assert result.fallback_organism['synonym'] == 'PerFile'

    def test_partial_config_fields(self, monkeypatch):
        """Only include/exclude fields work without other keys."""
        root = _make_file(1)
        leaf = _make_file(2, parent_id=1)
        leaf._path = [root, leaf]

        folder_data = {
            'include': [
                {'type': 'Gene', 'text': 'TP53', 'id': '7157', 'isCaseInsensitive': False}
            ],
        }
        svc = self._build_service_with_layers(
            monkeypatch, {root.id: _yaml_bytes(folder_data)}
        )
        result = svc.get_effective_annotation_config(leaf)
        assert len(result.custom_annotations) == 1
        assert result.custom_annotations[0]['text'] == 'TP53'
        assert result.annotation_configs is None
        assert result.fallback_organism is None

    def test_invalid_yaml_skipped(self, monkeypatch):
        """Invalid YAML content is silently skipped (returns empty config)."""
        root = _make_file(1)
        leaf = _make_file(2, parent_id=1)
        leaf._path = [root, leaf]

        svc = self._build_service_with_layers(
            monkeypatch, {root.id: b':\x00invalid yaml\xff'}
        )
        result = svc.get_effective_annotation_config(leaf)
        assert result.annotation_configs is None
        assert result.custom_annotations == []
