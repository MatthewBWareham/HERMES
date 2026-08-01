"""Minimal engine module for the URS cycle flow."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..operators.core import (
    CollapseOperator,
    CompleteOperator,
    GenerateOperator,
    IntegrateOperator,
    ReturnOperator,
    UnfoldOperator,
)
from ..schema.world_model import WorldModel

if TYPE_CHECKING:
    from ..execution.cycle_engine_driver import CycleEngineDriver
    from ..execution.world_model_loader import WorldModelLoader

# URS cohesion note: binds operators to the cycle engine.
# URS cohesion note: loads the world-model context into the execution layer.

MAX_RECURSION_DEPTH = 7
COLLAPSE_AVOIDANCE_ENABLED = True


class CycleEngine:
    """Execute the minimal URS reasoning cycle."""

    def __init__(self, world_model: WorldModel | None = None, recursion_limit: int = MAX_RECURSION_DEPTH) -> None:
        self.world_model = world_model or WorldModel()
        self.recursion_limit = recursion_limit

    def _check_recursion(self, depth: int) -> bool:
        return depth < self.recursion_limit

    def run(self, query: str, world_model: WorldModel | None = None, recursion_depth: int = 0) -> dict:
        if world_model is not None:
            self.world_model = world_model
        if not self._check_recursion(recursion_depth):
            raise RuntimeError("Recursion depth exceeds the URS limit of 7")

        state = {"query": query}
        operators = [
            ("generate", GenerateOperator()),
            ("unfold", UnfoldOperator()),
            ("collapse", CollapseOperator()),
            ("integrate", IntegrateOperator()),
            ("complete", CompleteOperator()),
            ("return", ReturnOperator()),
        ]

        for name, operator in operators:
            if name == "generate":
                state = operator.apply(query, self.world_model)
            elif name == "collapse":
                state = operator.apply(state, collapse_avoidance=COLLAPSE_AVOIDANCE_ENABLED)
            elif name == "integrate":
                state = operator.apply(state, self.world_model)
            else:
                state = operator.apply(state)

        self.world_model.add_operator_trace("cycle", input_state={"query": query}, output_state=state)
        self.world_model.recursion_depth = recursion_depth
        return state


__all__ = ["CycleEngine"]
