"""Global constants are stored here."""

from __future__ import annotations

from typing import Final

from tcod.event import KeySym

DIRECTION_KEYS: Final = {
    # Arrow keys
    KeySym.LEFT: (0, -1),
    KeySym.RIGHT: (0, 1),
    KeySym.UP: (-1, 0),
    KeySym.DOWN: (1, 0),
    # Keypad
    KeySym.KP_4: (0, -1),
    KeySym.KP_6: (0, 1),
    KeySym.KP_8: (-1, 0),
    KeySym.KP_2: (1, 0),
    KeySym.KP_7: (-1, -1),
    KeySym.KP_9: (-1, 1),
    KeySym.KP_1: (1, -1),
    KeySym.KP_3: (1, 1),
}