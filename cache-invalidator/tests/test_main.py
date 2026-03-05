import importlib
import json
import sys
from collections import defaultdict
from unittest.mock import MagicMock, call, patch

import pytest


@pytest.fixture
def main_module():
    """
    Import main.py with Redis and Neo4j connections fully mocked.

    Because main.py establishes connections at module level, we must patch
    the underlying connection constructors *before* the module is imported.
    This fixture handles module-level teardown so each test gets a clean state.
    """
    mock_redis = MagicMock()
    mock_redis.get.return_value = None

    mock_neo4j_driver = MagicMock()

    with (
        patch("redis.BlockingConnectionPool.from_url", return_value=MagicMock()),
        patch("redis.Redis", return_value=mock_redis),
        patch("neo4j.GraphDatabase.driver", return_value=mock_neo4j_driver),
        patch("neo4j.basic_auth", return_value=("neo4j", "password")),
    ):
        # Remove any previously cached version of the module so that the
        # patched constructors are used during import.
        sys.modules.pop("main", None)
        module = importlib.import_module("main")

        # Replace module-level singletons with our mock instances so that
        # functions referencing them at call time use the mocks too.
        module.redis_server = mock_redis
        module.neo4j_driver = mock_neo4j_driver

        yield module, mock_redis, mock_neo4j_driver

    sys.modules.pop("main", None)


# ---------------------------------------------------------------------------
# cache_data
# ---------------------------------------------------------------------------

def test_cache_data_sets_key(main_module):
    """cache_data should call redis SET with the JSON-serialised value."""
    module, mock_redis, _ = main_module

    module.cache_data("test_key", {"count": 42})

    args, _ = mock_redis.set.call_args
    assert args[0] == "test_key"
    assert json.loads(args[1]) == {"count": 42}


def test_cache_data_sets_expiry(main_module):
    """cache_data should call redis EXPIRE with the configured TTL."""
    module, mock_redis, _ = main_module

    module.cache_data("test_key", {"count": 42})

    mock_redis.expire.assert_called_once_with("test_key", module.CACHE_TTL)


def test_cache_data_disconnects_pool(main_module):
    """cache_data should disconnect the connection pool in the finally block."""
    module, mock_redis, _ = main_module

    module.cache_data("test_key", {})

    mock_redis.connection_pool.disconnect.assert_called_once()


# ---------------------------------------------------------------------------
# get_kg_statistics – label filtering logic
# ---------------------------------------------------------------------------

def test_get_kg_statistics_separates_domain_and_entity_labels(main_module):
    """
    Labels prefixed with 'db_' must be treated as domain labels; all other
    labels (except 'Synonym') must be treated as entity labels.
    """
    module, mock_redis, mock_neo4j_driver = main_module

    # Simulate db.labels() returning a mix of domain, entity and Synonym labels.
    label_rows = [
        {"label": "db_Human"},
        {"label": "db_Mouse"},
        {"label": "Gene"},
        {"label": "Disease"},
        {"label": "Synonym"},  # should be excluded from entity labels
    ]

    mock_session = MagicMock()
    mock_neo4j_driver.session.return_value = mock_session

    # First read_transaction → db.labels(); subsequent ones → entity counts
    count_result = [{"count": 0}]
    mock_session.read_transaction.side_effect = [
        label_rows,
        *([count_result] * 4),  # 2 domains × 2 entities = 4 count queries
    ]

    module.get_kg_statistics()

    # read_transaction is called once for db.labels() + once per domain/entity pair
    assert mock_session.read_transaction.call_count == 1 + 2 * 2


def test_get_kg_statistics_excludes_synonym_label(main_module):
    """'Synonym' should never appear as an entity label in the statistics."""
    module, mock_redis, mock_neo4j_driver = main_module

    label_rows = [
        {"label": "db_Human"},
        {"label": "Gene"},
        {"label": "Synonym"},
    ]

    mock_session = MagicMock()
    mock_neo4j_driver.session.return_value = mock_session

    # db.labels() + 1 domain × 1 entity = 2 read_transactions
    mock_session.read_transaction.side_effect = [
        label_rows,
        [{"count": 5}],
    ]

    result = module.get_kg_statistics()

    statistics = defaultdict(dict, result)
    for domain_stats in statistics.values():
        assert "Synonym" not in domain_stats


def test_get_kg_statistics_omits_zero_counts(main_module):
    """Entities with a count of zero should not appear in the statistics."""
    module, mock_redis, mock_neo4j_driver = main_module

    label_rows = [
        {"label": "db_Human"},
        {"label": "Gene"},
        {"label": "Disease"},
    ]

    mock_session = MagicMock()
    mock_neo4j_driver.session.return_value = mock_session

    mock_session.read_transaction.side_effect = [
        label_rows,
        [{"count": 10}],   # Human/Gene → should be included
        [{"count": 0}],    # Human/Disease → should be excluded
    ]

    result = module.get_kg_statistics()

    assert result["Human"]["Gene"] == 10
    assert "Disease" not in result.get("Human", {})
