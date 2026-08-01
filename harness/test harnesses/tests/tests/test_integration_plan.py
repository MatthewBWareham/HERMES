"""Integration tests for the Project HERMES orchestration scaffold."""

from runtime.engine.orchestrator import (
    build_world_model,
    evaluate_attractor_state,
    enforce_constraints,
    run_integrated_cycle,
)


def test_integration_helpers_exist():
    """The integration scaffold should expose placeholder helper functions."""
    assert callable(build_world_model)
    assert callable(evaluate_attractor_state)
    assert callable(enforce_constraints)
    assert callable(run_integrated_cycle)


def test_run_integrated_cycle_returns_metadata():
    """The orchestrator should return a structured metadata payload."""
    result = run_integrated_cycle("Test query")
    assert "result" in result
    assert "world_model" in result
    assert "constraints" in result
    assert "attractor" in result
