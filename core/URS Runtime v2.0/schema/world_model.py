"""Minimal world-model schema module for the URS runtime scaffold."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class IdentityLayer:
    """Represents a single identity layer in the URS identity architecture."""

    name: str
    value: Any
    confidence: float = 0.0


@dataclass
class Gradient:
    """Represents a scalar field gradient attached to the reasoning state."""

    name: str
    value: float
    description: Optional[str] = None


@dataclass
class StateNode:
    """Represents a state snapshot in the world-model."""

    name: str
    content: Dict[str, Any] = field(default_factory=dict)
    gradients: List[Gradient] = field(default_factory=list)


@dataclass
class Attractor:
    """Represents a stable attractor configuration."""

    name: str
    state: Dict[str, Any] = field(default_factory=dict)
    strength: float = 0.0


@dataclass
class Constraint:
    """Represents a logical or structural constraint."""

    name: str
    description: str
    satisfied: bool = True


@dataclass
class OperatorTrace:
    """Represents a recorded operator application."""

    operator_name: str
    input_state: Any
    output_state: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorldModel:
    """Minimal world-model state for the URS runtime scaffold."""

    concepts: List[Any] = field(default_factory=list)
    entities: List[Any] = field(default_factory=list)
    contexts: List[Any] = field(default_factory=list)
    relations: List[Tuple[Any, Any, str]] = field(default_factory=list)
    gradients: List[Gradient] = field(default_factory=list)
    states: List[StateNode] = field(default_factory=list)
    identity_layers: List[IdentityLayer] = field(default_factory=list)
    attractors: List[Attractor] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)
    narrative_nodes: List[StateNode] = field(default_factory=list)
    operator_history: List[OperatorTrace] = field(default_factory=list)
    recursion_depth: int = 0
    max_recursion_depth: int = 7

    def add_identity_layer(self, name: str, value: Any, confidence: float = 0.0) -> IdentityLayer:
        layer = IdentityLayer(name=name, value=value, confidence=confidence)
        self.identity_layers.append(layer)
        return layer

    def add_gradient(self, name: str, value: float, description: Optional[str] = None) -> Gradient:
        gradient = Gradient(name=name, value=value, description=description)
        self.gradients.append(gradient)
        return gradient

    def add_constraint(self, name: str, description: str, satisfied: bool = True) -> Constraint:
        constraint = Constraint(name=name, description=description, satisfied=satisfied)
        self.constraints.append(constraint)
        return constraint

    def add_operator_trace(self, operator_name: str, input_state: Any, output_state: Any, metadata: Optional[Dict[str, Any]] = None) -> OperatorTrace:
        trace = OperatorTrace(operator_name=operator_name, input_state=input_state, output_state=output_state, metadata=metadata or {})
        self.operator_history.append(trace)
        return trace


class WorldModelSchema:
    """Small schema declaration for the minimal URS world-model structure."""

    def __init__(self) -> None:
        self.fields = {
            "concepts": "Entities and concepts",
            "entities": "Reasoning entities",
            "contexts": "Situational context",
            "relations": "Entity relations",
            "gradients": "Reasoning gradients",
            "states": "Reasoning states",
            "identity_layers": "Core, narrative, and situational identity",
            "attractors": "Stable attractor states",
            "constraints": "Structural and logical constraints",
            "narrative_nodes": "Narrative state nodes",
            "operator_history": "Operator trace history",
            "recursion_depth": "Current recursion depth",
            "max_recursion_depth": "Maximum allowed recursion depth",
        }


__all__ = [
    "Attractor",
    "Constraint",
    "Gradient",
    "IdentityLayer",
    "OperatorTrace",
    "StateNode",
    "WorldModel",
    "WorldModelSchema",
]
