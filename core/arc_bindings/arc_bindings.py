"""Inert structural stub for URS arc bindings."""

from typing import Dict, Tuple

STRUCTURAL_ARC = "structural_arc"
ACTIVATION_ARC = "activation_arc"
EMERGENCE_ARC = "emergence_arc"
IDENTITY_ARC = "identity_arc"

ARC_BINDINGS: Dict[str, Tuple[str, ...]] = {
    STRUCTURAL_ARC: ("preactivation", "activation", "completion"),
    ACTIVATION_ARC: ("preactivation", "activation", "completion"),
    EMERGENCE_ARC: ("preactivation", "activation", "completion"),
    IDENTITY_ARC: ("preactivation", "activation", "completion"),
}
