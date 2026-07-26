"""Tests for the world-model schema."""

from runtime.world_model.schema import WorldModel, WorldModelSchema


def test_world_model_defaults():
    """The world-model should initialize with the expected container fields."""
    model = WorldModel()
    assert model.concepts == []
    assert model.states == []
    assert model.identity_layers == []
    assert model.attractors == []
    assert model.operator_history == []


def test_schema_contains_expected_fields():
    """The schema should describe the core architecture fields."""
    schema = WorldModelSchema()
    assert "identity_layers" in schema.fields
    assert "attractors" in schema.fields
    assert "operator_history" in schema.fields
