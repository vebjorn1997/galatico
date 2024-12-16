"""Base classes for states."""

from __future__ import annotations

import attrs
import tcod.console
import tcod.event
from tcod.event import KeySym

from game import g
from game.components import Gold, Graphic, Position, StarSystem, StarSystemEconomy
from game.constants import DIRECTION_KEYS
from game.tags import IsItem, IsPlayer
from game import menus
from game.state import StateResult, Reset, Push
from game import world_tools


@attrs.define()
class InGame:
    """Primary in-game state."""

    def on_event(self, event: tcod.event.Event) -> StateResult:
        """Handle events for the in-game state."""
        (player,) = g.world.Q.all_of(tags=[IsPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                player.components[Position] += DIRECTION_KEYS[sym]
                # Auto pickup gold
                for gold in g.world.Q.all_of(components=[Gold], tags=[player.components[Position], IsItem]):
                    player.components[Gold] += gold.components[Gold]
                    text = f"Picked up {gold.components[Gold]}g, total: {player.components[Gold]}g"
                    g.world[None].components[("Text", str)] = text
                    gold.clear()
                return None
            case tcod.event.KeyDown(sym=KeySym.ESCAPE):
                return Push(MainMenu())
            case _:
                return None

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the standard screen."""
        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y < console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.y, pos.x] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(x=0, y=console.height - 1, string=text, fg=(255, 255, 255), bg=(0, 0, 0))

# For record keeping, not used
class MainMenu(menus.ListMenu):
    """Main/escape menu."""

    __slots__ = ()

    def __init__(self) -> None:
        """Initialize the main menu."""
        items = [
            menus.SelectItem("New game", self.new_game),
            menus.SelectItem("Quit", self.quit),
        ]
        if hasattr(g, "world"):
            items.insert(0, menus.SelectItem("Continue", self.continue_))

        super().__init__(
            items=tuple(items),
            selected=0,
            x=1,
            y=1,
        )

    @staticmethod
    def continue_() -> StateResult:
        """Return to the game."""
        return Reset(InGame())

    @staticmethod
    def new_game() -> StateResult:
        """Begin a new game."""
        g.world = world_tools.new_universe()
        return Reset(DisplayAllSystems())

    @staticmethod
    def quit() -> StateResult:
        """Close the program."""
        raise SystemExit

class DisplayAllSystems(menus.ListMenu):
    """All systems menu."""

    __slots__ = ()

    def __init__(self) -> None:
        """Initialize the all systems menu."""
        systems = g.world.Q.all_of(components=[StarSystem])
        items = [
            menus.SelectItem(system.components[StarSystem].name, self.on_select(system)) for system in systems
        ]

        super().__init__(
            items=tuple(items),
            selected=0,
            x=1,
            y=1,
        )

    def on_select(self, system: StarSystem) -> StateResult:
        """Handle selection of a system."""
        def callback() -> StateResult:
            return Push(DisplaySystemDetails(system))
        return callback

class DisplaySystemDetails(menus.ListMenu):
    """Display system details."""

    def __init__(self, system: StarSystem) -> None:
        """Initialize the system details menu."""
        items = [
            menus.SelectItem(f"Name: {system.components[StarSystem].name}", None),
            menus.SelectItem(f"Construction Materials: {system.components[StarSystemEconomy].construction_materials}", None),
            menus.SelectItem(f"Food Stuff: {system.components[StarSystemEconomy].food_stuff}", None),
        ]
        super().__init__(
            items=tuple(items),
            selected=0,
            x=1,
            y=1,
        )
