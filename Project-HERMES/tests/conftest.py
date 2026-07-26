"""Test configuration for the HERMES project.

This ensures the repository root is available on ``sys.path`` so the runtime
and architecture packages import correctly during pytest collection.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
