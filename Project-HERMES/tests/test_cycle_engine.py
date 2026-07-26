"""Tests for the HERMES cycle engine."""

import pytest

from runtime.engine.cycle import CycleEngine


class DummyOperator:
    def __init__(self, result):
        self.result = result

    def apply(self, state):
        return self.result


def test_micro_cycle_runs_with_hooks():
    """micro_cycle should execute a single operator step and invoke hooks."""
    engine = CycleEngine()
    events = []

    def pre_hook(state, depth):
        events.append(("pre", state, depth))

    def post_hook(state, depth):
        events.append(("post", state, depth))

    result = engine.micro_cycle(
        DummyOperator("done"),
        "input",
        hooks={"pre": pre_hook, "post": post_hook},
        recursion_depth=1,
    )

    assert result == "done"
    assert events[0][0] == "pre"
    assert events[1][0] == "post"
