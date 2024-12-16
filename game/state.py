from __future__ import annotations

from typing import Protocol, TypeAlias

import attrs
import tcod.console
import tcod.event
from tcod.event import KeySym

from game import g
from game.world_tools import end_round


class State(Protocol):
    """An abstract game state."""

    __slots__ = ()

    def on_event(self, event: tcod.event.Event) -> StateResult:
        """Called on events."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Called when the state is being drawn."""


@attrs.define()
class Push:
    """Push a new state on top of the stack."""
    state: State


@attrs.define()
class Pop:
    """Remove the current state from the stack."""


@attrs.define()
class Reset:
    """Replace the entire stack with a new state."""
    state: State


StateResult: TypeAlias = "Push | Pop | Reset | None"
"""Union of state results."""

@attrs.define()
class EndRound(State):
    """End the round."""

    def on_event(self, event: tcod.event.Event) -> StateResult:
        """Handle events for the end round state."""
        match event:
            case tcod.event.KeyDown(sym=KeySym.SPACE):
                return end_round(g.world)
    
    def on_draw(self, console: tcod.console.Console) -> None:
        pass