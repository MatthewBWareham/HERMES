"""Tests for the attractor-state implementation."""

from architecture.dynamics.attractor_state import AttractorState


def test_attractor_state_basin_function_is_thresholded():
    """A high-coherence state should score strongly within the attractor basin."""
    attractor = AttractorState(name="coherence", optimization_threshold=0.7)
    score = attractor.basin_function(0.9, 0.2)
    assert score >= 0.0
    assert score <= 1.0


def test_attractor_state_reports_basin_boundaries():
    """The attractor should expose basin lower/upper boundaries around its threshold."""
    attractor = AttractorState(name="coherence", optimization_threshold=0.7, basin_geometry={"width": 0.2, "depth": 0.3})
    boundaries = attractor.basin_boundaries()
    assert boundaries["lower"] < 0.7
    assert boundaries["upper"] > 0.7


def test_attractor_state_detects_stability():
    """A state above threshold and with low entropy should be stable."""
    attractor = AttractorState(name="coherence", optimization_threshold=0.7)
    assert attractor.is_stable(0.9, 0.1, 0.9) is True


def test_attractor_state_detects_instability():
    """A low-coherence state should fail stability checks."""
    attractor = AttractorState(name="coherence", optimization_threshold=0.7)
    assert attractor.is_stable(0.5, 0.8, 0.6) is False
