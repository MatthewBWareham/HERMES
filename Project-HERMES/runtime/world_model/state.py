"""Lightweight state objects for micro- and macro-level reasoning.

These structures capture local and global reasoning states, historical traces,
and potential future states needed by the runtime engine in the unified theory
runtime model.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class IdentityState:
    """A lightweight representation of identity within the world-model."""
    name: str
    value: Any
    confidence: float = 0.0


@dataclass
class ReasoningState:
    """Represents a reasoning state within the HERMES world-model."""
    name: str
    content: Dict[str, Any] = field(default_factory=dict)
    identity: Optional[IdentityState] = None
    history: List[Dict[str, Any]] = field(default_factory=list)

    def add_history_entry(self, entry: Dict[str, Any]) -> None:
        """Append a lightweight history entry to the state."""
        self.history.append(entry)

    def to_dict(self) -> Dict[str, Any]:
        """Return a compact dictionary representation for runtime use."""
        return {
            "name": self.name,
            "content": self.content,
            "identity": self.identity.to_dict() if self.identity is not None else None,
            "history": self.history,
        }


@dataclass
class IdentityStateContainer:
    """A small container for multiple identity layers or viewpoints."""
    layers: List[IdentityState] = field(default_factory=list)

    def add_layer(self, name: str, value: Any, confidence: float = 0.0) -> IdentityState:
        """Add a lightweight identity layer to the container."""
        layer = IdentityState(name=name, value=value, confidence=confidence)
        self.layers.append(layer)
        return layer
