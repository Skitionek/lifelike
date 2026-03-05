import sys
from unittest.mock import MagicMock

# ``graphdb.py`` and ``rcache.py`` import and instantiate connections at
# module level.  We must inject mocks for these external packages *before*
# any test module triggers the import chain so that collection succeeds
# without running external services.

# Only mock the modules that are not yet present (i.e. not really installed
# in the test environment).  This keeps the real implementations in place
# when the full dependency set is installed (e.g. inside a pipenv shell).

for _module in ("neo4j",):
    if _module not in sys.modules:
        sys.modules[_module] = MagicMock()

# Patch neo4j.GraphDatabase.driver at the attribute level so that the
# driver instantiation in graphdb.py does not attempt a real connection.
import neo4j  # noqa: E402 – may be real or the mock above
neo4j.GraphDatabase.driver = MagicMock(return_value=MagicMock())
neo4j.basic_auth = MagicMock(return_value=("neo4j", "password"))
