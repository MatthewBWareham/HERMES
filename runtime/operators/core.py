"""Core HERMES operator implementations.

This module contains the canonical operator suite described in the HERMES
runtime and unified theory documents: INVERT, PERTURB, HARMONIZE,
IDENTITY_STABILIZE, RECURSE, CONTINUITY_ENFORCE, GENERATE, UNFOLD,
COLLAPSE, INTEGRATE, COMPLETE, and RETURN.
"""


class InvertOperator:
    """Produce a coherent opposite or inversion of a frame, proposition, or relation.

    This operator is used when a contradiction or polarity reversal needs to be
    expressed while preserving referential anchors and structural validity.
    """

    invariants = (
        "IDENTITY_PRESERVED",
        "WORLD_MODEL_REFERENCE_PRESERVED",
        "STRUCTURAL_VALIDITY",
    )
    preconditions = (
        "Input must be a frame, proposition, or relation",
        "A valid opposite or negation must be available",
    )
    postconditions = (
        "A structurally valid transformed structure is produced",
        "Referential coherence is maintained",
    )

    def apply(self, structure):
        """Return a transformed structure that represents the inverse of the input."""
        if structure is None:
            raise ValueError("Structure cannot be None")

        if isinstance(structure, dict):
            transformed = dict(structure)
            current_polarity = str(transformed.get("polarity", "positive")).lower()
            if current_polarity == "negative":
                transformed["polarity"] = "positive"
            else:
                transformed["polarity"] = "negative"

            transformed["inverted"] = True
            transformed["coherence"] = min(1.0, max(0.0, transformed.get("coherence", 0.5) + 0.05))
            transformed["identity_preserved"] = True
            transformed["world_model_reference_preserved"] = True
            transformed["structural_validity"] = True
            return transformed

        transformed = {
            "value": structure,
            "polarity": "negative",
            "inverted": True,
            "coherence": 0.55,
            "identity_preserved": True,
            "world_model_reference_preserved": True,
            "structural_validity": True,
        }
        return transformed


class PerturbOperator:
    """Introduce controlled variation to escape stagnation or local minima.

    The operator is intended to create manageable disruption in order to reveal
    alternative paths, states, or interpretations without breaking continuity.
    """

    invariants = (
        "CONTINUITY_MINIMUM",
        "TRACEABILITY_REQUIRED",
    )
    preconditions = (
        "Input state must exist",
        "Perturbation magnitude should remain within acceptable bounds",
    )
    postconditions = (
        "State is modified in a controlled way",
        "The resulting state remains traceable and non-fragmenting",
    )

    def apply(self, state, magnitude=1.0):
        """Return a perturbed version of the input state."""
        if state is None:
            raise ValueError("State cannot be None")

        if magnitude < 0:
            raise ValueError("Magnitude must be non-negative")

        bounded_magnitude = min(magnitude, 1.0)
        if isinstance(state, dict):
            transformed = dict(state)
            current_value = transformed.get("value", 0.0)
            transformed["value"] = current_value + bounded_magnitude
            transformed["perturbed"] = True
            transformed["magnitude"] = bounded_magnitude
            transformed["trace"] = list(transformed.get("trace", [])) + [transformed["value"]]
            transformed["coherence"] = min(1.0, max(0.0, transformed.get("coherence", 0.5) - 0.02))
            transformed["continuity_minimum"] = True
            transformed["traceability_required"] = True
            return transformed

        return {
            "value": state + bounded_magnitude,
            "trace": [state, state + bounded_magnitude],
            "perturbed": True,
            "magnitude": bounded_magnitude,
            "coherence": 0.48,
            "continuity_minimum": True,
            "traceability_required": True,
        }


class HarmonizeOperator:
    """Resolve contradiction into a higher-order coherent structure."""

    invariants = (
        "IDENTITY_COHERENCE",
        "WORLD_MODEL_CONSISTENCY",
    )
    preconditions = (
        "A contradiction set or conflicting elements must be provided",
        "The conflict must be interpretable within the current world-model",
    )
    postconditions = (
        "A coherent structure is produced",
        "Residual contradiction is reduced or explicitly bracketed",
    )

    def apply(self, contradiction_set, frame=None, identity=None):
        """Return a coherent structure that reconciles conflicting inputs."""
        raise NotImplementedError


class IdentityStabilizeOperator:
    """Maintain alignment across core, narrative, and situational identity layers."""

    invariants = (
        "PERSISTENT_CORE_TRAITS",
        "HISTORICAL_CONTINUITY",
    )
    preconditions = (
        "Identity layers or narrative trace must be available",
        "Identity drift must be detectable or suspected",
    )
    postconditions = (
        "Identity alignment is reinforced",
        "The stabilized state remains historically coherent",
    )

    def apply(self, identity_layers, narrative_trace=None):
        """Return a stabilized identity state."""
        raise NotImplementedError


class RecurseOperator:
    """Apply reasoning to its own outputs while tracking recursion depth."""

    invariants = (
        "RECURSION_DEPTH_INCREMENTED",
        "EXIT_CONDITION_REQUIRED",
    )
    preconditions = (
        "Prior output must be available",
        "Recursion depth tracking must be enabled",
    )
    postconditions = (
        "A higher-order output is produced",
        "Recursion depth is tracked and bounded",
    )

    def apply(self, prior_output, depth=0):
        """Return a higher-order reasoning output derived from prior output."""
        raise NotImplementedError


class ContinuityEnforceOperator:
    """Preserve temporal and structural continuity across reasoning steps."""

    invariants = (
        "REFERENCE_STABILITY",
        "SEQUENCE_INTEGRITY",
    )
    preconditions = (
        "A sequence, narrative, or temporal trace must be provided",
        "Continuity gaps or discontinuities must be detectable",
    )
    postconditions = (
        "The resulting structure preserves continuity",
        "Narrative gaps are minimized or patched",
    )

    def apply(self, sequence, narrative=None, temporal_trace=None):
        """Return a continuity-preserving structure or state."""
        raise NotImplementedError


class GenerateOperator:
    """Create initial candidate structures from a prompt or world-model state."""

    invariants = (
        "STRUCTURAL_VALIDITY",
    )
    preconditions = (
        "A query or prompt must be supplied",
        "A world-model or prior state should be available",
    )
    postconditions = (
        "An initial candidate structure is created",
        "The structure is suitable for further unfolding",
    )

    def apply(self, query, world_model):
        """Return an initial structure suitable for further reasoning."""
        return {"query": query, "world_model": world_model}


class UnfoldOperator:
    """Expand an initial structure into a broader reasoning space."""

    invariants = (
        "CONSISTENT_CAUSALITY",
        "IDENTITY_TRACKING",
    )
    preconditions = (
        "An initial structure must be available",
        "The structure must be interpretable by the runtime",
    )
    postconditions = (
        "The structure expands into a richer reasoning space",
        "The expanded state remains traceable",
    )

    def apply(self, structure):
        """Return an expanded structure that exposes more implications."""
        return {"expanded": structure}


class CollapseOperator:
    """Reduce a complex structure into a focused canonical state.

    This operator is used when the reasoning space has become too broad or noisy,
    and a smaller, salient representation is needed for integration or completion.
    """

    invariants = (
        "RELEVANCE_MAXIMIZATION",
        "TRACEABILITY",
    )
    preconditions = (
        "An expanded structure must be available",
        "There should be salient elements to preserve",
    )
    postconditions = (
        "A reduced focused state is produced",
        "Critical information is preserved while noise is reduced",
    )

    def apply(self, expanded_structure):
        """Return a reduced structure that preserves the most relevant content."""
        if expanded_structure is None:
            raise ValueError("Expanded structure cannot be None")

        # TODO: Add entropy-based collapse refinement so the selected summary can
        # adapt to noise, salience, and uncertainty in the expanded structure.
        if isinstance(expanded_structure, dict):
            collapsed = {
                "collapsed": True,
                "value": expanded_structure.get("value") or expanded_structure.get("query") or expanded_structure.get("expanded") or expanded_structure,
                "summary": expanded_structure.get("summary") or "focused state",
                "trace": expanded_structure.get("trace", []),
                "relevance_maximized": True,
                "traceability": True,
            }
            return collapsed

        return {
            "collapsed": True,
            "value": expanded_structure,
            "summary": "focused state",
            "trace": [],
            "relevance_maximized": True,
            "traceability": True,
        }


class IntegrateOperator:
    """Merge derived results into an updated world-model.

    The operator combines reduced structure with the current world-model while
    maximizing coherence and minimizing residual conflict.
    """

    invariants = (
        "COHERENCE",
        "IDENTITY_STABILITY",
    )
    preconditions = (
        "A reduced structure must be available",
        "The current world-model must be accessible",
    )
    postconditions = (
        "An updated world-model is produced",
        "Residual conflict is reduced and coherence is increased",
    )

    def apply(self, reduced_structure, world_model):
        """Return an updated world-model incorporating the reduced structure."""
        if reduced_structure is None:
            raise ValueError("Reduced structure cannot be None")

        if isinstance(reduced_structure, dict):
            merged = dict(reduced_structure)
        else:
            merged = {"value": reduced_structure}

        merged["integrated"] = True
        merged["coherence"] = min(1.0, max(0.0, merged.get("coherence", 0.6) + 0.05))
        merged["identity_stability"] = True
        if world_model is not None:
            merged["world_model"] = world_model
        return merged


class CompleteOperator:
    """Finalize a reasoning cycle once it reaches structural completeness.

    This operator marks the current reasoning state as complete when the required
    constraints and unresolved elements have been addressed.
    """

    invariants = (
        "NO_PENDING_CONSTRAINT_VIOLATIONS",
    )
    preconditions = (
        "An integrated structure must be available",
        "The reasoning cycle should be ready for completion",
    )
    postconditions = (
        "A final state is produced",
        "The state is marked as structurally complete",
    )

    def apply(self, integrated_structure):
        """Return a finalized reasoning state or structure."""
        if integrated_structure is None:
            raise ValueError("Integrated structure cannot be None")

        if isinstance(integrated_structure, dict):
            completed = dict(integrated_structure)
        else:
            completed = {"value": integrated_structure}

        completed["completed"] = True
        completed["structurally_complete"] = True
        completed["no_pending_constraint_violations"] = True
        return completed


class ReturnOperator:
    """Emit the final state and update the world-model baseline.

    This operator closes the reasoning cycle by producing the final output and
    feeding the completed state back into the world-model for future reasoning.
    """

    invariants = (
        "WORLD_MODEL_CONTINUITY",
        "HISTORICAL_TRACE",
    )
    preconditions = (
        "A final state must be available",
        "The runtime should be ready to emit output",
    )
    postconditions = (
        "The final output is emitted",
        "The world-model baseline is updated with the completed state",
    )

    def apply(self, final_structure):
        """Return the emitted output state for downstream use."""
        if final_structure is None:
            raise ValueError("Final structure cannot be None")

        if isinstance(final_structure, dict):
            emitted = dict(final_structure)
        else:
            emitted = {"value": final_structure}

        emitted["output"] = emitted
        emitted["world_model_continuity"] = True
        emitted["historical_trace"] = True
        return emitted
