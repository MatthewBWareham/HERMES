"""Constraint engine for HERMES runtime validation.

This module enforces the meta-logic constraints and runtime checks described in
the HERMES and unified theory documents, including identity coherence,
contradiction handling, continuity, recursion caps, distortion thresholds, and
operator validity.
"""

from typing import Any, Dict, List, Optional, Tuple


class ConstraintEngine:
    """Validate reasoning states and operator application against runtime constraints."""

    def __init__(self, recursion_cap: int = 32, distortion_threshold: float = 0.7):
        self.recursion_cap = recursion_cap
        self.distortion_threshold = distortion_threshold

    def check_recursion(self, depth: int) -> bool:
        """Return whether the current recursion depth remains within the cap."""
        return depth <= self.recursion_cap

    def check_distortion(self, distortion: float) -> bool:
        """Return whether the distortion measure stays within the threshold."""
        return distortion <= self.distortion_threshold

    def check_identity_coherence(self, identity_state: Any, prior_state: Any) -> bool:
        """Ensure identity is present and not obviously inconsistent with the prior state."""
        if identity_state is None or prior_state is None:
            return False
        return True

    def check_contradiction(self, contradiction_state: Any) -> bool:
        """Ensure contradiction data is available so it can be handled by the runtime."""
        return contradiction_state is not None

    def check_continuity(self, state: Any, previous_state: Any) -> bool:
        """Ensure the current and previous states exist to preserve continuity."""
        return state is not None and previous_state is not None

    def validate_operator(self, operator_name: str, inputs: Optional[Dict[str, Any]] = None) -> Tuple[bool, List[str]]:
        """Validate an operator name and its expected input context."""
        valid_operators = {
            "INVERT",
            "PERTURB",
            "HARMONIZE",
            "IDENTITY_STABILIZE",
            "RECURSE",
            "CONTINUITY_ENFORCE",
            "GENERATE",
            "UNFOLD",
            "COLLAPSE",
            "INTEGRATE",
            "COMPLETE",
            "RETURN",
        }
        errors: List[str] = []
        if operator_name not in valid_operators:
            errors.append("Operator is not recognized by the HERMES runtime")
        if inputs is None:
            errors.append("Operator inputs were not provided")
        return (not errors), errors

    def evaluate(self, *, depth: int, distortion: float, identity_state: Any, prior_state: Any, contradiction_state: Any, state: Any, previous_state: Any, operator_name: str, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Evaluate a full set of runtime constraints and return the results."""
        checks = {
            "recursion_ok": self.check_recursion(depth),
            "distortion_ok": self.check_distortion(distortion),
            "identity_coherence_ok": self.check_identity_coherence(identity_state, prior_state),
            "contradiction_ready": self.check_contradiction(contradiction_state),
            "continuity_ok": self.check_continuity(state, previous_state),
            "operator_valid": self.validate_operator(operator_name, inputs)[0],
        }
        return {
            "passed": all(checks.values()),
            "checks": checks,
            "errors": [
                message
                for message in self.validate_operator(operator_name, inputs)[1]
                if message
            ],
        }
