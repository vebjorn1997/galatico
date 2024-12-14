"""This module stores globally mutable variables used by this game."""

from __future__ import annotations

import tcod.context
import tcod.console
import tcod.ecs

from game.state import State

context: tcod.context.Context
"""The window managed by tcod."""

world: tcod.ecs.Registry
"""The active ECS registry and current session."""

states: list[State] = []
"""A stack of states with the last item being the active state."""

console: tcod.console.Console
"""The current main console."""