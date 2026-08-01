"""World-model schema definitions for HERMES.

This module defines the conceptual structure of the world-model used by the
runtime and unified cognitive architecture, including concepts, entities,
relations, contexts, gradients, states, narrative nodes, attractors, identity
layers, constraints, recursion depth tracking, and operator history.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class IdentityLayer:
    """Represents one layer of identity within the unified cognitive architecture."""
    name: str
    value: Any
    confidence: float = 0.0


@dataclass
class Gradient:
    """A scalar or vector-like gradient attached to a state or structure."""
    name: str
    value: float
    description: Optional[str] = None


@dataclass
class StateNode:
    """A discrete reasoning or narrative state in the world-model."""
    name: str
    content: Dict[str, Any] = field(default_factory=dict)
    gradients: List[Gradient] = field(default_factory=list)


@dataclass
class Attractor:
    """A stable or resonant configuration toward which the system may converge."""
    name: str
    state: Dict[str, Any] = field(default_factory=dict)
    strength: float = 0.0


@dataclass
class Constraint:
    """A logical or structural requirement that must be preserved."""
    name: str
    description: str
    satisfied: bool = True


@dataclass
class OperatorTrace:
    """A single recorded step in the reasoning history."""
    operator_name: str
    input_state: Any
    output_state: Any
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorldModel:
    """Container for the core reasoning substrate of HERMES."""
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
    max_recursion_depth: int = 32

    def add_identity_layer(self, name: str, value: Any, confidence: float = 0.0) -> IdentityLayer:
        """Add a new identity layer to the world-model."""
        layer = IdentityLayer(name=name, value=value, confidence=confidence)
        self.identity_layers.append(layer)
        return layer

    def add_gradient(self, name: str, value: float, description: Optional[str] = None) -> Gradient:
        """Attach a gradient such as coherence, entropy, relevance, or certainty."""
        gradient = Gradient(name=name, value=value, description=description)
        self.gradients.append(gradient)
        return gradient

    def add_attractor(self, name: str, state: Dict[str, Any], strength: float = 0.0) -> Attractor:
        """Record a stable attractor configuration toward which the system may converge."""
        attractor = Attractor(name=name, state=state, strength=strength)
        self.attractors.append(attractor)
        return attractor

    def add_constraint(self, name: str, description: str, satisfied: bool = True) -> Constraint:
        """Register a structural or logical constraint that must be preserved."""
        constraint = Constraint(name=name, description=description, satisfied=satisfied)
        self.constraints.append(constraint)
        return constraint

    def add_operator_trace(self, operator_name: str, input_state: Any, output_state: Any, metadata: Optional[Dict[str, Any]] = None) -> OperatorTrace:
        """Append a trace entry describing an operator application."""
        trace = OperatorTrace(operator_name=operator_name, input_state=input_state, output_state=output_state, metadata=metadata or {})
        self.operator_history.append(trace)
        return trace

    def initialize_identity(self, core_value: Any = "core", narrative_value: Any = "narrative", situational_value: Any = "situational") -> None:
        """Populate the identity layers with default core, narrative, and situational identities."""
        self.add_identity_layer("core", core_value, confidence=1.0)
        self.add_identity_layer("narrative", narrative_value, confidence=0.9)
        self.add_identity_layer("situational", situational_value, confidence=0.8)

    def initialize_gradients(self, coherence: float = 0.7, entropy: float = 0.2, relevance: float = 0.5, certainty: float = 0.6) -> None:
        """Populate common reasoning gradients used by the architecture."""
        self.add_gradient("coherence", coherence, description="reasoning coherence")
        self.add_gradient("entropy", entropy, description="reasoning entropy")
        self.add_gradient("relevance", relevance, description="salience")
        self.add_gradient("certainty", certainty, description="confidence")

    def initialize_constraints(self) -> None:
        """Populate the standard meta-logic constraints for the runtime."""
        self.add_constraint("identity_coherence", "Identity layers must remain aligned")
        self.add_constraint("continuity", "Reasoning must preserve continuity")
        self.add_constraint("contradiction_handling", "Contradictions must be resolved or reframed")


class WorldModelSchema:
    """Schema definition for the minimal world-model structure."""

    def __init__(self):
        self.fields = {
            "concepts": "Explicit conceptual nodes",
            "entities": "Objects with identity and attributes",
            "contexts": "Situational frames",
            "relations": "Explicit, emergent, and meta-relations",
            "gradients": "Coherence, entropy, relevance, certainty",
            "states": "Micro-state and macro-state snapshots",
            "identity_layers": "Core, narrative, and situational identity",
            "attractors": "Stable or resonant configurations",
            "constraints": "Structural, logical, and identity constraints",
            "narrative_nodes": "Story-like reasoning structures",
            "operator_history": "Trace of operator steps and transformations",
            "recursion_depth": "Current recursion level",
            "max_recursion_depth": "Maximum allowed recursion depth",
        }
        self.architecture_notes = {
            "identity": "Supports multiple identity layers for core, narrative, and situational identity",
            "gradients": "Tracks coherence, entropy, relevance, and certainty gradients",
            "attractors": "Stores attractor states that reflect stable reasoning basins",
            "constraints": "Captures runtime meta-logic constraints and their satisfaction status",
            "operator_history": "Records operator applications as a trace for inspectable reasoning",
        }
