from celestial_bodies import System
from utils import get_star_names

class GameState():
    def __init__(self):
        self.systems = []
        self.generate_universe()

    def generate_universe(self):
        star_names = get_star_names()
        for star in star_names:
            self.add_system(System(star))

    def add_system(self, system: System):
        self.systems.append(system)

    def count_planets(self):
        return sum(len(system.planets) for system in self.systems)