"""Example: run a minimal HERMES reasoning cycle with a simple world-model."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.engine.cycle import CycleEngine
from runtime.world_model import WorldModel


def main() -> None:
    world_model = WorldModel()
    world_model.add_identity("core", "self", confidence=1.0)
    world_model.add_gradient("coherence", 0.8, description="initial coherence")
    world_model.add_gradient("entropy", 0.2, description="initial entropy")

    engine = CycleEngine(world_model=world_model)
    result = engine.run("simple query")

    print("Cycle result:")
    print(result)
    print("\nWorld-model identities:")
    for identity in world_model.identities:
        print(f"- {identity.name}: {identity.value} (confidence={identity.confidence})")


if __name__ == "__main__":
    main()
