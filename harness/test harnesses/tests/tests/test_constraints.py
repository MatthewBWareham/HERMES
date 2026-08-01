"""Tests for the HERMES constraint engine."""

from runtime.constraints.engine import ConstraintEngine


def test_constraint_engine_accepts_valid_operator():
    """The engine should accept recognized operators with provided inputs."""
    engine = ConstraintEngine()
    result = engine.evaluate(
        depth=5,
        distortion=0.2,
        identity_state="stable",
        prior_state="stable",
        contradiction_state="none",
        state="current",
        previous_state="previous",
        operator_name="INVERT",
        inputs={"structure": "frame"},
    )
    assert result["passed"] is True


def test_constraint_engine_rejects_invalid_operator():
    """The engine should reject unknown operators."""
    engine = ConstraintEngine()
    result = engine.evaluate(
        depth=40,
        distortion=0.9,
        identity_state=None,
        prior_state=None,
        contradiction_state=None,
        state=None,
        previous_state=None,
        operator_name="UNKNOWN",
        inputs={"structure": "frame"},
    )
    assert result["passed"] is False
