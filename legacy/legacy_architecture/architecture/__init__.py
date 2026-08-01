"""Compatibility shim for the repository-level architecture package."""

from pathlib import Path

__path__ = [
    str(Path(__file__).resolve().parent),
    str(Path(__file__).resolve().parent.parent / "HERMES_code" / "architecture"),
]
