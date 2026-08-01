"""Integration-style tests for runtime operator, cycle, world-model, and attractor behavior."""

from architecture.dynamics.attractor_state import AttractorState
from runtime.engine.cycle import CycleEngine
from runtime.operators.core import InvertOperator, PerturbOperator
from runtime.world_model.schema import WorldModel


def test_invert_operator_flips_polarity_and_marks_inversion():
    """InvertOperator should preserve the anchor while flipping polarity and increasing coherence."""
    operator = InvertOperator()
    result = operator.apply({"value": "A", "polarity": "positive", "coherence": 0.6})

    assert result["polarity"] == "negative"
    assert result["inverted"] is True
    assert result["coherence"] >= 0.6


def test_perturb_operator_clamps_magnitude_and_records_trace():
    """PerturbOperator should clamp large magnitudes and retain a breadcrumb trace."""
    operator = PerturbOperator()
    result = operator.apply({"value": 1.0, "trace": [1.0], "coherence": 0.7}, magnitude=3.0)

    assert result["value"] == 2.0
    assert result["trace"] == [1.0, 2.0]
    assert result["perturbed"] is True


def test_cycle_engine_preserves_world_model_reference_and_records_updates():
    """The cycle engine should keep the live world-model object and record each step."""
    world_model = WorldModel()
    engine = CycleEngine(world_model=world_model, coherence_threshold=0.0, entropy_limit=1.0)

    result = engine.micro_cycle(
        PerturbOperator(),
        {"value": 1.0, "coherence": 0.9, "entropy": 0.1},
        operator_args=({"value": 1.0, "coherence": 0.9, "entropy": 0.1}, 0.2),
    )

    assert result["value"] == 1.2
    assert engine.world_model is world_model
    assert len(world_model.operator_history) == 1
    assert world_model.operator_history[-1].output_state == result


def test_world_model_initializers_and_attractor_stability_capture_runtime_state():
    """The world-model helpers should seed runtime state and the attractor should distinguish stable and unstable states."""
    world_model = WorldModel()
    world_model.initialize_identity()
    world_model.initialize_gradients()
    world_model.initialize_constraints()

    attractor = AttractorState(name="coherence", optimization_threshold=0.7)

    assert [layer.name for layer in world_model.identity_layers] == ["core", "narrative", "situational"]
    assert {gradient.name for gradient in world_model.gradients} >= {"coherence", "entropy", "relevance", "certainty"}
    assert len(world_model.constraints) == 3
    assert attractor.is_stable(0.8, 0.1, 0.8) is True
    assert attractor.is_stable(0.6, 0.8, 0.6) is False
