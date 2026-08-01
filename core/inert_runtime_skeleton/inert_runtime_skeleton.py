"""Inert structural stub exposing the unified URS runtime skeleton."""

from typing import Dict, Any

from .integration_spine import IntegrationSpine
from .arc_bindings import ARC_BINDINGS
from .coherence_map import COHERENCE_MAP

INERT_RUNTIME_SKELETON: Dict[str, Any] = {
    "integration_spine": IntegrationSpine,
    "arc_bindings": ARC_BINDINGS,
    "coherence_map": COHERENCE_MAP,
}
