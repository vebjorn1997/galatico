from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from game import g
import game.states
import game.world_tools


def main():
    tileset = tcod.tileset.load_tilesheet(
        "data/tileset/dejavu16x16_gs_tc.png",
        32,
        8,
        tcod.tileset.CHARMAP_TCOD,
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    g.console = tcod.console.Console(50, 35, order="F")
    state = game.states.InGame()
    g.world = game.world_tools.new_world()

    with tcod.context.new(
        columns=g.console.width,
        rows=g.console.height,
        tileset=tileset,
    ) as g.context:
        while True:
            g.console.clear()
            state.on_draw(g.console)
            g.context.present(g.console)
            for event in tcod.event.wait():
                state.on_event(event)
                # if isinstance(event, tcod.event.Quit):
                #     raise SystemExit()


if __name__ == "__main__":
    main()
