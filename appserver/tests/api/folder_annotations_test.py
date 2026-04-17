"""API tests for folder-level .annotations endpoints."""
import hashlib
import json
import types

import pytest
import yaml

from neo4japp.constants import FILE_MIME_TYPE_ANNOTATIONS
from neo4japp.models import AppUser, Files, Projects, AppRole, projects_collaborator_role, FileContent
from neo4japp.services.file_types.providers import DirectoryTypeProvider
from neo4japp.services.elastic import ElasticService
from datetime import datetime


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def generate_headers(jwt_token):
    return {'Authorization': f'Bearer {jwt_token}'}


def _yaml_body(data: dict) -> bytes:
    return yaml.dump(data, allow_unicode=True).encode('utf-8')


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope='function')
def mock_elastic(monkeypatch):
    monkeypatch.setattr(ElasticService, 'index_files', lambda *a, **kw: None)
    monkeypatch.setattr(ElasticService, 'delete_files', lambda *a, **kw: None)
    monkeypatch.setattr(ElasticService, 'index_maps', lambda *a, **kw: None)


@pytest.fixture(scope='function')
def fix_admin_role_fa(session):
    from neo4japp.services import AccountService
    svc = AccountService()
    return svc.get_or_create_role('admin')


@pytest.fixture(scope='function')
def fix_superuser_role_fa(session):
    from neo4japp.services import AccountService
    svc = AccountService()
    return svc.get_or_create_role('private-data-access')


@pytest.fixture(scope='function')
def admin_user(session, fix_admin_role_fa, fix_superuser_role_fa) -> AppUser:
    user = AppUser(
        id=501,
        username='fa_admin',
        email='fa_admin@lifelike.bio',
        first_name='FA',
        last_name='Admin',
    )
    user.set_password('password')
    user.roles.extend([fix_admin_role_fa, fix_superuser_role_fa])
    session.add(user)
    session.flush()
    return user


@pytest.fixture(scope='function')
def fix_folder(session, admin_user) -> Files:
    """A root directory with its project."""
    root = Files(
        filename='/',
        mime_type=DirectoryTypeProvider.MIME_TYPE,
        user=admin_user,
    )
    project = Projects(
        name='folder-annot-test',
        description='test',
        root=root,
        creation_date=datetime.now(),
    )
    session.add(root)
    session.add(project)
    session.flush()

    role = AppRole.query.filter(AppRole.name == 'project-admin').one()
    session.execute(
        projects_collaborator_role.insert(),
        [{'appuser_id': admin_user.id, 'app_role_id': role.id, 'projects_id': project.id}],
    )
    session.flush()
    return root


def login_as_user(self, email, password):
    resp = self.post(
        '/auth/login',
        data=json.dumps({'email': email, 'password': password}),
        content_type='application/json',
    )
    return resp.get_json()


@pytest.fixture(scope='function')
def client(app):
    c = app.test_client()
    c.login_as_user = types.MethodType(login_as_user, c)
    return c


# ---------------------------------------------------------------------------
# Tests: GET folder-annotations (no file yet)
# ---------------------------------------------------------------------------

class TestFolderAnnotationsGetEmpty:
    def test_returns_empty_when_no_annotations_file(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        response = client.get(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            headers=headers,
        )
        assert response.status_code == 200
        assert response.get_json() == {}


# ---------------------------------------------------------------------------
# Tests: PUT folder-annotations (create / replace)
# ---------------------------------------------------------------------------

class TestFolderAnnotationsPut:
    def test_create_annotations_file(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        payload = {
            'fallback_organism': {'synonym': 'Homo sapiens', 'taxonomy_id': '9606'},
            'exclude': [
                {'type': 'Disease', 'text': 'cancer', 'isCaseInsensitive': True, 'reason': 'generic'}
            ],
        }

        response = client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(payload),
            content_type='application/yaml',
            headers=headers,
        )
        assert response.status_code == 200
        result = response.get_json()
        assert result['fallback_organism']['synonym'] == 'Homo sapiens'
        assert len(result['exclude']) == 1

    def test_replace_existing_annotations_file(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        first_payload = {'fallback_organism': {'synonym': 'E.coli', 'taxonomy_id': '511145'}}
        client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(first_payload),
            content_type='application/yaml',
            headers=headers,
        )

        second_payload = {'fallback_organism': {'synonym': 'Homo sapiens', 'taxonomy_id': '9606'}}
        response = client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(second_payload),
            content_type='application/yaml',
            headers=headers,
        )
        assert response.status_code == 200
        assert response.get_json()['fallback_organism']['synonym'] == 'Homo sapiens'

    def test_invalid_yaml_returns_400(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        response = client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=b': invalid: yaml: content: !!python/object:builtins.dict',
            content_type='application/yaml',
            headers=headers,
        )
        # Should fail with 400 (invalid YAML or schema validation error)
        assert response.status_code in (400, 422)


# ---------------------------------------------------------------------------
# Tests: PATCH folder-annotations (partial update)
# ---------------------------------------------------------------------------

class TestFolderAnnotationsPatch:
    def test_patch_merges_into_existing(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        initial = {
            'fallback_organism': {'synonym': 'E.coli', 'taxonomy_id': '511145'},
            'annotation_configs': {
                'exclude_references': True,
                'annotation_methods': {'Gene': {'nlp': False, 'rules_based': True}},
            },
        }
        client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(initial),
            content_type='application/yaml',
            headers=headers,
        )

        patch_data = {
            'annotation_configs': {
                'annotation_methods': {'Disease': {'nlp': True, 'rules_based': False}},
            },
        }
        response = client.patch(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(patch_data),
            content_type='application/yaml',
            headers=headers,
        )
        assert response.status_code == 200
        result = response.get_json()
        methods = result['annotation_configs']['annotation_methods']
        # Both Gene and Disease should be present after merge
        assert 'Gene' in methods
        assert 'Disease' in methods
        # Original fallback_organism should be preserved
        assert result['fallback_organism']['synonym'] == 'E.coli'


# ---------------------------------------------------------------------------
# Tests: DELETE folder-annotations
# ---------------------------------------------------------------------------

class TestFolderAnnotationsDelete:
    def test_delete_existing_annotations_file(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        payload = {'fallback_organism': {'synonym': 'E.coli', 'taxonomy_id': '511145'}}
        client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(payload),
            content_type='application/yaml',
            headers=headers,
        )

        del_response = client.delete(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            headers=headers,
        )
        assert del_response.status_code == 204

        # GET should now return empty again
        get_response = client.get(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            headers=headers,
        )
        assert get_response.status_code == 200
        assert get_response.get_json() == {}

    def test_delete_non_existing_is_idempotent(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        response = client.delete(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            headers=headers,
        )
        assert response.status_code == 204


# ---------------------------------------------------------------------------
# Tests: GET effective-annotations-config
# ---------------------------------------------------------------------------

class TestEffectiveAnnotationsConfig:
    def test_returns_empty_config_with_no_annotations(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        response = client.get(
            f'/filesystem/objects/{hash_id}/effective-annotations-config',
            headers=headers,
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data.get('customAnnotations', []) == []
        assert data.get('excludedAnnotations', []) == []

    def test_returns_merged_config_after_put(
            self, client, admin_user, fix_folder, mock_elastic, session):
        resp_login = client.login_as_user(admin_user.email, 'password')
        headers = generate_headers(resp_login['accessToken']['token'])
        hash_id = fix_folder.hash_id

        payload = {
            'fallback_organism': {'synonym': 'Homo sapiens', 'taxonomy_id': '9606'},
        }
        client.put(
            f'/filesystem/objects/{hash_id}/folder-annotations',
            data=_yaml_body(payload),
            content_type='application/yaml',
            headers=headers,
        )

        response = client.get(
            f'/filesystem/objects/{hash_id}/effective-annotations-config',
            headers=headers,
        )
        assert response.status_code == 200
        data = response.get_json()
        # fallbackOrganism should be present from folder config
        fo = data.get('fallbackOrganism')
        assert fo is not None
        assert fo['synonym'] == 'Homo sapiens'
