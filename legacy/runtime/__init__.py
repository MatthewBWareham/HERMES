"""Minimal URS runtime package scaffold."""

from .urs_runtime import (
    COLLAPSE_AVOIDANCE_ENABLED,
    MAX_RECURSION_DEPTH,
    OPERATOR_CHAIN,
    URSRuntime,
)

__all__ = [
    "COLLAPSE_AVOIDANCE_ENABLED",
    "MAX_RECURSION_DEPTH",
    "OPERATOR_CHAIN",
    "URSRuntime",
]
