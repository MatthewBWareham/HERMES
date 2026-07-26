"""Tests for attractor-state mathematics."""

from architecture.dynamics.optimizer import stability_check


def test_stability_check_reports_stable_state():
    """A high-coherence, low-entropy state should be considered stable."""
    stable, details = stability_check(0.9, 0.2, 0.9)
    assert stable is True
    assert details["noise_ratio"] >= 0


def test_stability_check_reports_unstable_state():
    """A low-coherence or high-entropy state should be considered unstable."""
    stable, _ = stability_check(0.3, 0.9, 0.4)
    assert stable is False
