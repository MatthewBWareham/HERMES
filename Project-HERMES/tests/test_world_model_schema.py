"""Tests for the populated world-model schema."""

from runtime.world_model.schema import WorldModel


def test_world_model_supports_identity_and_gradient_helpers():
    """The world-model should support adding identity layers, gradients, attractors, constraints, and traces."""
    model = WorldModel()
    model.add_identity_layer("core", "self", confidence=0.95)
    model.add_gradient("coherence", 0.9, description="reasoning coherence")
    model.add_attractor("stable_state", {"coherence": 0.9}, strength=0.8)
    model.add_constraint("continuity", "must be preserved", satisfied=True)
    model.add_operator_trace("INVERT", {"value": "A"}, {"value": "A", "polarity": "negative"})

    assert len(model.identity_layers) == 1
    assert len(model.gradients) == 1
    assert len(model.attractors) == 1
    assert len(model.constraints) == 1
    assert len(model.operator_history) == 1
