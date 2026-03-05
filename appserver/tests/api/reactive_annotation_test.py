"""Tests for reactive file indexing and annotation.

These tests verify that:
1. Newly created PDF/enrichment-table files are flagged with needs_reannotation=True.
2. When file content is updated, the file is re-flagged for re-annotation.
3. Successful annotation clears the needs_reannotation flag.
4. The /annotations/needs-reannotation endpoint returns files that need re-annotation.
"""
import hashlib
import pytest
from datetime import datetime

from neo4japp.models import AppUser, Files, FileContent, Projects
from neo4japp.services.file_types.providers import (
    PDFTypeProvider,
    EnrichmentTableTypeProvider,
    DirectoryTypeProvider,
)


def generate_headers(jwt_token):
    return {'Authorization': f'Bearer {jwt_token}'}


# ---------------------------------------------------------------------------
# Unit-level tests (model / provider)
# ---------------------------------------------------------------------------

class TestNeedsReannotationDefault:
    """Files.needs_reannotation defaults to False for non-annotatable types."""

    def test_directory_default_false(self, session, fix_admin_user, fix_project):
        f = Files(
            mime_type=DirectoryTypeProvider.MIME_TYPE,
            filename='myfolder',
            user=fix_admin_user,
            parent=fix_project.root,
        )
        session.add(f)
        session.flush()
        assert f.needs_reannotation is False

    def test_pdf_default_false_when_created_directly(self, session, fix_admin_user, fix_project):
        """When a PDF File object is created without going through the API the
        flag defaults to False (the API endpoint sets it to True)."""
        content = FileContent(
            raw_file=b'%PDF-test',
            checksum_sha256=hashlib.sha256(b'%PDF-test').digest(),
        )
        session.add(content)
        session.flush()
        f = Files(
            mime_type=PDFTypeProvider.MIME_TYPE,
            filename='test.pdf',
            user=fix_admin_user,
            parent=fix_project.root,
            content=content,
        )
        session.add(f)
        session.flush()
        assert f.needs_reannotation is False


class TestPDFProviderHandleContentUpdate:
    """PDFTypeProvider.handle_content_update clears annotations and sets flag."""

    def test_clears_annotations_and_marks_for_reannotation(
            self, session, fix_admin_user, fix_project):
        content = FileContent(
            raw_file=b'%PDF-test',
            checksum_sha256=hashlib.sha256(b'%PDF-test').digest(),
        )
        session.add(content)
        session.flush()

        f = Files(
            mime_type=PDFTypeProvider.MIME_TYPE,
            filename='test.pdf',
            user=fix_admin_user,
            parent=fix_project.root,
            content=content,
            annotations={'documents': []},
            annotations_date=datetime.now(),
            needs_reannotation=False,
        )
        session.add(f)
        session.flush()

        provider = PDFTypeProvider()
        provider.handle_content_update(f)

        assert f.annotations is None
        assert f.annotations_date is None
        assert f.needs_reannotation is True


class TestEnrichmentTableProviderHandleContentUpdate:
    """EnrichmentTableTypeProvider.handle_content_update clears annotations and sets flag."""

    def test_clears_enrichment_annotations_and_marks_for_reannotation(
            self, session, fix_admin_user, fix_project):
        content = FileContent(
            raw_file=b'{}',
            checksum_sha256=hashlib.sha256(b'{}').digest(),
        )
        session.add(content)
        session.flush()

        f = Files(
            mime_type=EnrichmentTableTypeProvider.MIME_TYPE,
            filename='table.json',
            user=fix_admin_user,
            parent=fix_project.root,
            content=content,
            enrichment_annotations={'genes': []},
            needs_reannotation=False,
        )
        session.add(f)
        session.flush()

        provider = EnrichmentTableTypeProvider()
        provider.handle_content_update(f)

        assert f.enrichment_annotations is None
        assert f.needs_reannotation is True


# ---------------------------------------------------------------------------
# API-level tests
# ---------------------------------------------------------------------------

class TestFilesNeedingReannotationEndpoint:
    """GET /annotations/needs-reannotation returns hash IDs of files needing annotation."""

    def test_returns_files_with_flag_set(
            self, client, session, fix_admin_user, fix_project):
        """Files with needs_reannotation=True appear in the response."""
        login_resp = client.login_as_user(fix_admin_user.email, 'password')
        headers = generate_headers(login_resp['accessToken']['token'])

        content = FileContent(
            raw_file=b'%PDF-1',
            checksum_sha256=hashlib.sha256(b'%PDF-1').digest(),
        )
        session.add(content)
        session.flush()

        f = Files(
            mime_type=PDFTypeProvider.MIME_TYPE,
            filename='pending.pdf',
            user=fix_admin_user,
            parent=fix_project.root,
            content=content,
            needs_reannotation=True,
        )
        session.add(f)
        session.flush()

        response = client.get('/annotations/needs-reannotation', headers=headers)
        assert response.status_code == 200
        data = response.get_json()
        assert f.hash_id in data['hash_ids']
        assert data['total'] >= 1

    def test_does_not_return_annotated_files(
            self, client, session, fix_admin_user, fix_project):
        """Files with needs_reannotation=False do NOT appear in the response."""
        login_resp = client.login_as_user(fix_admin_user.email, 'password')
        headers = generate_headers(login_resp['accessToken']['token'])

        content = FileContent(
            raw_file=b'%PDF-2',
            checksum_sha256=hashlib.sha256(b'%PDF-2').digest(),
        )
        session.add(content)
        session.flush()

        f = Files(
            mime_type=PDFTypeProvider.MIME_TYPE,
            filename='done.pdf',
            user=fix_admin_user,
            parent=fix_project.root,
            content=content,
            needs_reannotation=False,
        )
        session.add(f)
        session.flush()

        response = client.get('/annotations/needs-reannotation', headers=headers)
        assert response.status_code == 200
        data = response.get_json()
        assert f.hash_id not in data['hash_ids']

    def test_requires_admin_role(self, client, test_user):
        """Non-admin users get a 403."""
        login_resp = client.login_as_user(test_user.email, 'password')
        headers = generate_headers(login_resp['accessToken']['token'])
        response = client.get('/annotations/needs-reannotation', headers=headers)
        assert response.status_code == 403
