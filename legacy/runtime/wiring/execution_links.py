"""Minimal placeholder stub for execution wiring."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..execution.cycle_engine_driver import CycleEngineDriver
    from ..execution.world_model_loader import WorldModelLoader

# URS cohesion note: links the execution layer to the cycle-engine and world-model wiring surface.


class ExecutionLinks:
    """Placeholder structural stub for execution links."""

    name = "execution_links"
