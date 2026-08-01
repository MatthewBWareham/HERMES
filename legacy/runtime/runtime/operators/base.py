"""Base abstractions for HERMES operators.

This module defines the common interface for atomic transformations such as
INVERT, PERTURB, HARMONIZE, and other reasoning operators described in the
HERMES runtime documents.
"""


class Operator:
    """Abstract base class for runtime operators."""

    def apply(self, state):
        """Apply an operator transform to a given state."""
        raise NotImplementedError
