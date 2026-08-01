"""Attractor-state definitions for HERMES dynamics.

This module encodes the optimization threshold, basin geometry, entropy
gradients, and stability conditions described in the runtime and unified
cognitive architecture documents as a minimal attractor model.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


def entropy_gradient(coherence: float, entropy: float) -> float:
    """Return a simple entropy-pressure gradient from coherence and entropy."""
    return max(0.0, entropy - coherence)


def noise_ratio(signal: float, noise: float) -> float:
    """Return a normalized noise ratio for the signal/noise pair."""
    if signal + noise == 0:
        return 0.0
    return noise / (signal + noise)


@dataclass
class AttractorState:
    """Represents a stable or resonant state toward which reasoning may converge."""
    name: str
    optimization_threshold: float = 0.7
    basin_geometry: Dict[str, float] = field(default_factory=lambda: {"width": 1.0, "depth": 1.0})
    entropy_gradient: float = 0.0
    stability_conditions: List[str] = field(default_factory=lambda: ["coherence", "continuity", "identity_alignment"])
    metadata: Optional[Dict[str, object]] = None

    def _normalized_value(self, value: float) -> float:
        """Clamp a value into the [0, 1] optimization range."""
        return max(0.0, min(1.0, value))

    def basin_boundaries(self) -> Dict[str, float]:
        """Return the lower and upper basin boundaries around the optimization threshold."""
        width = max(0.01, self.basin_geometry.get("width", 1.0))
        return {
            "lower": max(0.0, self.optimization_threshold - width),
            "upper": min(1.0, self.optimization_threshold + width),
            "width": width,
            "depth": max(0.01, self.basin_geometry.get("depth", 1.0)),
        }

    def basin_function(self, coherence: float, entropy: float) -> float:
        """Compute a simple attractor score around the optimization threshold."""
        coherence = self._normalized_value(coherence)
        entropy = self._normalized_value(entropy)
        width = max(0.01, self.basin_geometry.get("width", 1.0))
        # TODO: Add attractor-transition logic with hysteresis and basin hopping
        # so the system can move between competing stable states more gracefully.
        depth = max(0.01, self.basin_geometry.get("depth", 1.0))
        threshold = self.optimization_threshold

        centered = coherence - threshold
        penalty = entropy * depth
        score = 1.0 - (centered * centered) / max(width, 0.01) - penalty
        return max(0.0, min(1.0, score))

    def threshold_crossing(self, coherence: float, entropy: float) -> bool:
        """Return True when the state crosses the attractor threshold."""
        score = self.basin_function(coherence, entropy)
        return score >= self.optimization_threshold

    def is_stable(self, coherence: float, entropy: float, identity_alignment: float) -> bool:
        """Return whether the attractor state satisfies its stability conditions."""
        coherence = self._normalized_value(coherence)
        entropy = self._normalized_value(entropy)
        identity_alignment = self._normalized_value(identity_alignment)

        if coherence < self.optimization_threshold:
            return False
        if entropy > max(0.0, self.entropy_gradient or self.optimization_threshold):
            return False
        if identity_alignment < self.optimization_threshold:
            return False
        return self.threshold_crossing(coherence, entropy)

    def basin_score(self, coherence: float, entropy: float) -> float:
        """Compute a simple basin score based on coherence and entropy."""
        return self.basin_function(coherence, entropy)

    def stability_score(self, coherence: float, entropy: float, identity_alignment: float) -> Dict[str, float]:
        """Return a compact set of attractor metrics for the current state."""
        coherence = self._normalized_value(coherence)
        entropy = self._normalized_value(entropy)
        identity_alignment = self._normalized_value(identity_alignment)
        return {
            "coherence": coherence,
            "entropy": entropy,
            "identity_alignment": identity_alignment,
            "basin_score": self.basin_score(coherence, entropy),
            "threshold": self.optimization_threshold,
        }
