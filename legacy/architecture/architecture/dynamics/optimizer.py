"""Optimization-threshold attractor mathematics for HERMES.

This module encodes the attractor behavior described in the runtime and
architectural documents using simple mathematical definitions for:
- noise ratios
- entropy gradients
- basin boundaries
- stability checks
"""

from typing import Dict, Tuple


def noise_ratio(signal: float, noise: float) -> float:
    """Compute a normalized noise ratio for a signal/noise pair."""
    if signal + noise == 0:
        return 0.0
    return noise / (signal + noise)


def entropy_gradient(coherence: float, entropy: float) -> float:
    """Approximate the entropy gradient from coherence and entropy values."""
    return max(0.0, entropy - coherence)


def coherence_gradient(coherence: float, identity_alignment: float, entropy: float) -> float:
    """Approximate the coherence gradient from alignment and entropy pressure."""
    return max(0.0, coherence - identity_alignment - entropy)


def distortion_threshold(coherence: float, entropy: float, threshold: float = 0.7) -> float:
    """Compute a simple distortion threshold based on coherence and entropy drift."""
    return max(0.0, threshold - coherence + entropy)


def basin_boundaries(threshold: float, width: float = 1.0, depth: float = 1.0) -> Dict[str, float]:
    """Return simple basin boundary values around the optimization threshold."""
    lower = max(0.0, threshold - width)
    upper = threshold + width
    return {
        "lower": lower,
        "upper": upper,
        "width": width,
        "depth": depth,
    }


def stability_check(
    coherence: float,
    entropy: float,
    identity_alignment: float,
    threshold: float = 0.7,
    entropy_limit: float = 0.8,
) -> Tuple[bool, Dict[str, float]]:
    """Evaluate whether a reasoning state satisfies the attractor stability conditions."""
    # TODO: Expand this check with richer attractor-transition behavior and
    # multi-step coherence tracking for sequential reasoning runs.
    noise = noise_ratio(coherence, entropy)
    gradient = entropy_gradient(coherence, entropy)
    boundaries = basin_boundaries(threshold)

    stable = (
        coherence >= threshold
        and identity_alignment >= threshold
        and entropy <= entropy_limit
        and gradient <= entropy_limit
        and boundaries["lower"] <= coherence <= boundaries["upper"]
    )

    return stable, {
        "noise_ratio": noise,
        "entropy_gradient": gradient,
        "threshold": threshold,
        "entropy_limit": entropy_limit,
        "boundaries": boundaries,
    }
