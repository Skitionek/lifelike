import sys
import os

# Ensure the cache-invalidator root directory is in the path so that
# ``import main`` (which is at the root, not inside a package) works
# regardless of which directory pytest is invoked from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
