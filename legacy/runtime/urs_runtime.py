"""Minimal URS runtime entrypoint for the repository scaffold."""

from __future__ import annotations

from .engine.cycle import CycleEngine
from .operators.core import (
    CollapseOperator,
    CompleteOperator,
    GenerateOperator,
    IntegrateOperator,
    ReturnOperator,
    UnfoldOperator,
)
from .schema.world_model import WorldModel, WorldModelSchema

MAX_RECURSION_DEPTH = 7
COLLAPSE_AVOIDANCE_ENABLED = True
OPERATOR_CHAIN = (
    "GENERATE",
    "UNFOLD",
    "COLLAPSE",
    "INTEGRATE",
    "COMPLETE",
    "RETURN",
)


class URSRuntime:
    """Lightweight runtime adapter over the canonical cycle engine."""

    def __init__(self, world_model: WorldModel | None = None) -> None:
        self.world_model = world_model or WorldModel()
        self.engine = CycleEngine(world_model=self.world_model)

    def run(self, query: str, *, recursion_depth: int = 0):
        """Execute the minimal URS cycle over a user query."""
        return self.engine.run(query, world_model=self.world_model, recursion_depth=recursion_depth)


__all__ = [
    "COLLAPSE_AVOIDANCE_ENABLED",
    "MAX_RECURSION_DEPTH",
    "OPERATOR_CHAIN",
    "CycleEngine",
    "CollapseOperator",
    "CompleteOperator",
    "GenerateOperator",
    "IntegrateOperator",
    "ReturnOperator",
    "UnfoldOperator",
    "URSRuntime",
    "WorldModel",
    "WorldModelSchema",
]
