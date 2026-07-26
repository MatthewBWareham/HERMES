"""Tests for HERMES operator stubs."""

import pytest

from runtime.operators.core import (
    CollapseOperator,
    CompleteOperator,
    IntegrateOperator,
    InvertOperator,
    PerturbOperator,
    ReturnOperator,
)


@pytest.mark.parametrize(
    "operator_cls",
    [CollapseOperator, CompleteOperator, IntegrateOperator, ReturnOperator],
)
def test_operator_has_contract_attributes(operator_cls):
    """Each operator should expose invariants, preconditions, and postconditions."""
    assert hasattr(operator_cls, "invariants")
    assert hasattr(operator_cls, "preconditions")
    assert hasattr(operator_cls, "postconditions")


def test_invert_operator_returns_inverted_structure():
    """InvertOperator should preserve the input label while flipping its polarity."""
    operator = InvertOperator()
    result = operator.apply({"value": "A", "polarity": "positive"})
    assert result["polarity"] == "negative"
    assert result["value"] == "A"


def test_invert_operator_reverses_existing_negative_polarity():
    """InvertOperator should reverse an already-negated polarity to a coherent opposite."""
    operator = InvertOperator()
    result = operator.apply({"value": "A", "polarity": "negative"})
    assert result["polarity"] == "positive"


def test_invert_operator_marks_runtime_invariants():
    """InvertOperator should make its invariant guarantees explicit in the returned structure."""
    operator = InvertOperator()
    result = operator.apply({"value": "A", "polarity": "positive", "identity": "self", "world_model_reference": "state-1"})

    assert result["identity_preserved"] is True
    assert result["world_model_reference_preserved"] is True
    assert result["structural_validity"] is True


def test_perturb_operator_modifies_state_in_boundaries():
    """PerturbOperator should create a bounded change without losing traceability."""
    operator = PerturbOperator()
    result = operator.apply({"value": 2.0, "trace": [1.0]}, magnitude=0.5)
    assert result["value"] == 2.5
    assert result["trace"] == [1.0, 2.5]
