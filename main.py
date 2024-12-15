from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from game import g
import game.states
import game.world_tools
import game.state_tools


def main():
    tileset = tcod.tileset.load_tilesheet(
        "data/tileset/dejavu16x16_gs_tc.png",
        32,
        8,
        tcod.tileset.CHARMAP_TCOD,
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    g.console = tcod.console.Console(50, 35, order="F")
    g.states = [game.states.MainMenu()]

    with tcod.context.new(
        columns=g.console.width,
        rows=g.console.height,
        tileset=tileset,
    ) as g.context:
        while True:
            game.state_tools.main_draw()
            for event in tcod.event.wait():
                game.state_tools.apply_state_result(g.states[-1].on_event(event))


if __name__ == "__main__":
    main()
