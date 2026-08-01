"""Cycle engine for the HERMES reasoning loop.

This module orchestrates the canonical reasoning cycle described in the unified
cognitive architecture documents: GENERATE -> UNFOLD -> COLLAPSE -> INTEGRATE
-> COMPLETE -> RETURN. It also supports micro-cycle execution for smaller,
local reasoning passes.
"""

import logging

from runtime.operators.core import (
    CollapseOperator,
    CompleteOperator,
    GenerateOperator,
    IntegrateOperator,
    ReturnOperator,
    UnfoldOperator,
)


logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(message)s")


class CycleEngine:
    """Coordinates reasoning stages and state transitions across a cycle."""

    def __init__(self, world_model=None, coherence_threshold=0.6, entropy_limit=0.9, logger_instance=None):
        """Initialize the engine with a world-model and runtime thresholds."""
        self.world_model = world_model
        self.coherence_threshold = coherence_threshold
        self.entropy_limit = entropy_limit
        self.recursion_limit = 32
        self.current_state = None
        self.history = []
        self.logger = logger_instance or logger

    def _check_entropy(self, state):
        """Check entropy with a very small guard. TODO: replace with richer policy logic."""
        if isinstance(state, dict):
            entropy = state.get("entropy", 0.0)
            return entropy <= self.entropy_limit
        return True

    def _check_coherence(self, state):
        """Check coherence with a very small guard. TODO: replace with richer policy logic."""
        if isinstance(state, dict):
            coherence = state.get("coherence", 1.0)
            return coherence >= self.coherence_threshold
        return True

    def _check_recursion(self, depth):
        """Placeholder recursion limit check. TODO: add explicit depth policy."""
        return depth < self.recursion_limit

    def _update_world_model(self, state):
        """Record the latest step in the attached world-model when available."""
        if self.world_model is None:
            return None

        if hasattr(self.world_model, "add_operator_trace"):
            self.world_model.add_operator_trace(
                "cycle_step",
                input_state=self.current_state,
                output_state=state,
                metadata={"history_length": len(self.history)},
            )
            self.logger.info("World model updated: recorded operator trace (%d total)", len(self.history))
        if hasattr(self.world_model, "add_gradient"):
            self.world_model.add_gradient("coherence", self.coherence_threshold, description="runtime coherence threshold")
        if hasattr(self.world_model, "add_gradient"):
            self.world_model.add_gradient("entropy", self.entropy_limit, description="runtime entropy limit")
        if hasattr(self.world_model, "add_constraint"):
            self.world_model.add_constraint("cycle_progression", "state must satisfy coherence and entropy guards")
        self.logger.info("World model updated: coherence=%s entropy=%s", self.coherence_threshold, self.entropy_limit)
        return self.world_model

    def micro_cycle(self, operator, input_state, *, hooks=None, recursion_depth=0, operator_args=None):
        """Execute one operator step and record the result."""
        hooks = hooks or {}
        pre_hook = hooks.get("pre")
        post_hook = hooks.get("post")
        error_hook = hooks.get("error")

        if pre_hook is not None:
            pre_hook(input_state, recursion_depth)

        operator_name = getattr(operator, "__class__", type(operator)).__name__
        self.logger.info("Running operator: %s (depth=%s)", operator_name, recursion_depth)

        try:
            if not self._check_entropy(input_state):
                raise RuntimeError("Entropy threshold exceeded")
            if not self._check_coherence(input_state):
                raise RuntimeError("Coherence threshold not met")
            if not self._check_recursion(recursion_depth):
                raise RuntimeError("Recursion limit exceeded")

            if operator_args is None:
                result = operator.apply(input_state)
            else:
                result = operator.apply(*operator_args)

            self.current_state = result
            self.history.append(result)
            self._update_world_model(result)
            self.logger.info("Operator completed: %s", operator_name)

            if post_hook is not None:
                post_hook(result, recursion_depth)
            return result
        except Exception as exc:
            if error_hook is not None:
                error_hook(exc, input_state, recursion_depth)
            raise

    def run(self, query, world_model=None, recursion_depth=0):
        """Run the simple operator-driven cycle for a query."""
        if world_model is not None:
            self.world_model = world_model

        operators = [
            ("generate", GenerateOperator()),
            ("unfold", UnfoldOperator()),
            ("collapse", CollapseOperator()),
            ("integrate", IntegrateOperator()),
            ("complete", CompleteOperator()),
            ("return", ReturnOperator()),
        ]

        state = {"query": query, "world_model": self.world_model}
        self.logger.info("Starting reasoning cycle for query: %s", query)
        # TODO: Introduce multi-cycle coherence checks that compare successive
        # cycles, detect drift, and decide whether the engine should re-enter
        # perturbation or integration before completion.
        for index, (name, operator) in enumerate(operators):
            if name == "generate":
                self.logger.info("Stage %s: generate", index)
                state = self.micro_cycle(
                    operator,
                    state,
                    recursion_depth=recursion_depth + index,
                    operator_args=(query, self.world_model),
                )
            elif name == "integrate":
                self.logger.info("Stage %s: integrate", index)
                state = self.micro_cycle(
                    operator,
                    state,
                    recursion_depth=recursion_depth + index,
                    operator_args=(state, self.world_model),
                )
            else:
                self.logger.info("Stage %s: %s", index, name)
                state = self.micro_cycle(
                    operator,
                    state,
                    recursion_depth=recursion_depth + index,
                )

        self.current_state = state
        self.history.append(state)
        self._update_world_model(state)
        self.logger.info("Reasoning cycle complete")
        return state
