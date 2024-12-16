import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity
from typing import Final

@attrs.define(frozen=True)
class Position:
    """An entities position."""

    x: int
    y: int

    def __add__(self, direction: tuple[int, int]):
        """Add a vector to this position."""
        x, y = direction
        return self.__class__(self.x + x, self.y + y)

@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed(entity: Entity, old: Position | None, new: Position | None) -> None:
    """Mirror position components as a tag."""

    if old == new:  # New position is equivalent to its previous value
        return  # Ignore and return
    if old is not None:  # Position component removed or changed
        entity.tags.discard(old)  # Remove old position from tags
    if new is not None:  # Position component added or changed
        entity.tags.add(new)  # Add new position to tags

@attrs.define(frozen=True)
class Graphic:
    """An entities icon and color."""

    ch: int = ord("!")
    fg: tuple[int, int, int] = (255, 255, 255)

@attrs.define(frozen=True)
class StarSystem:
    """A star system."""

    name: str

@attrs.define(frozen=True)
class StarSystemEconomy:
    """A star system's economy."""

    construction_materials: int # Everything from minerals to synthetic materials
    food_stuff: int


Gold: Final = ("Gold", int)
"""Amount of gold."""