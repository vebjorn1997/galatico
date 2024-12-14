import tcod
from abc import ABC, abstractmethod

class ControlBase(ABC):
    @abstractmethod
    def on_draw(self, console: tcod.console.Console):
        pass

    @abstractmethod
    def on_event(self, event: tcod.event.Event):
        pass

class ControlSystems(ControlBase):
    # def __init__(self, gamestate: GameState):
    #     self.gamestate = gamestate

    def on_draw(self, console: tcod.console.Console):
        pass
        # for i, system in enumerate(self.gamestate.systems):
        #     console.print(0, i, f"{i}: {system.name}")

    def on_event(self, event: tcod.event.Event):
        pass

class ControlPanel(ControlBase):
    menues = ["View all Systems", "Quit"]
    def on_draw(self, console: tcod.console.Console):
        for i, item in enumerate(self.menues):
            console.print(0, i, f"{i}: {item}")

    def on_event(self, event: tcod.event.Event):
        if isinstance(event, tcod.event.KeyDown):
            if event.sym == tcod.event.KeySym.N1:
                print("List of Systems!")