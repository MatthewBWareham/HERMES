"""Lightweight world-model structures for the HERMES runtime.

These structures mirror the Unified Cognitive Architecture document in a compact
form, providing identity layers, reasoning states, and gradients that can be
used across operators, cycle engines, and attractor logic.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Identity:
    """A lightweight identity layer for the cognitive architecture."""
    name: str
    value: Any
    confidence: float = 0.0


@dataclass
class State:
    """A lightweight reasoning or narrative state in the world-model."""
    name: str
    content: Dict[str, Any] = field(default_factory=dict)
    identity: Optional[Identity] = None
    history: List[Dict[str, Any]] = field(default_factory=list)

    def add_history_entry(self, entry: Dict[str, Any]) -> None:
        """Append a small history entry to the state."""
        self.history.append(entry)


@dataclass
class Gradient:
    """A scalar gradient used to track coherence, entropy, relevance, or certainty."""
    name: str
    value: float = 0.0
    description: Optional[str] = None


@dataclass
class WorldModel:
    """A lightweight container representing the runtime world-model."""
    identities: List[Identity] = field(default_factory=list)
    states: List[State] = field(default_factory=list)
    gradients: List[Gradient] = field(default_factory=list)

    def add_identity(self, name: str, value: Any, confidence: float = 0.0) -> Identity:
        """Add an identity layer to the world-model."""
        identity = Identity(name=name, value=value, confidence=confidence)
        self.identities.append(identity)
        return identity

    def add_state(self, name: str, content: Optional[Dict[str, Any]] = None) -> State:
        """Add a reasoning state to the world-model."""
        state = State(name=name, content=content or {})
        self.states.append(state)
        return state

    def add_gradient(self, name: str, value: float = 0.0, description: Optional[str] = None) -> Gradient:
        """Add a gradient such as coherence or entropy."""
        gradient = Gradient(name=name, value=value, description=description)
        self.gradients.append(gradient)
        return gradient
