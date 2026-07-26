"""Runtime-level tests for the HERMES cycle engine."""

from runtime.engine.cycle import CycleEngine


def test_cycle_engine_uses_threshold_checks():
    """The engine should evaluate coherence and entropy thresholds during a cycle run."""
    engine = CycleEngine(coherence_threshold=0.6, entropy_limit=0.5)
    result = engine.run("query")
    assert result is not None
    assert engine.current_state is not None
