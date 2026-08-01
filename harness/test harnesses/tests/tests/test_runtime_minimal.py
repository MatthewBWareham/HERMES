"""Minimal smoke tests for core runtime behavior."""

from architecture.dynamics.attractor_state import AttractorState
from runtime.engine.cycle import CycleEngine
from runtime.operators.core import InvertOperator


def test_invert_operator_flips_polarity_and_marks_invariants():
    """InvertOperator should reverse polarity and expose the documented invariants."""
    operator = InvertOperator()
    result = operator.apply({"value": "A", "polarity": "positive"})

    assert result["polarity"] == "negative"
    assert result["identity_preserved"] is True
    assert result["structural_validity"] is True


def test_attractor_state_reports_stability():
    """The attractor should mark a coherent, low-entropy state as stable."""
    attractor = AttractorState(name="coherence", optimization_threshold=0.7)

    assert attractor.is_stable(0.9, 0.1, 0.9) is True
    assert attractor.is_stable(0.5, 0.8, 0.6) is False


def test_cycle_engine_runs_and_tracks_state():
    """The cycle engine should execute and retain the resulting state."""
    engine = CycleEngine()
    result = engine.run("query")

    assert result is not None
    assert engine.current_state is result
    assert len(engine.history) >= 1
