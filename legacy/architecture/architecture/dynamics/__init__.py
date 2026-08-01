"""Dynamic equilibrium and transition management for HERMES architecture."""

from .attractor_state import AttractorState
from .optimizer import (
    basin_boundaries,
    coherence_gradient,
    distortion_threshold,
    entropy_gradient,
    noise_ratio,
    stability_check,
)
