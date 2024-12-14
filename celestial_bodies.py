import random
from utils import get_planet_names

class System():
    def __init__(self, name):
        self.name = name
        self.planets: list[CelestialBody] = []
        self.generate_planets()

    def generate_planets(self):
        for _ in range(random.randint(1, 4)):
            planet = CelestialBody(get_planet_names(), self)
            self.planets.append(planet)

    def __str__(self):
        return f"{self.name} is a star"

class BodyEconomyStats():
    def __init__(self, body: "CelestialBody", eco_size: float, pop_size_in_mil: int, tech_level: int):
        self.body = body
        self.eco_size = eco_size
        self.pop_size = pop_size_in_mil
        self.tech_level = tech_level
        self.eco_growth = self.calculate_eco_growth()

    def calculate_eco_growth(self):
        return self.pop_size * self.tech_level

    def __str__(self):
        return f"{self.body.name} has an economic size of {self.eco_size}, an economic growth of {self.eco_growth}, a population size of {self.pop_size}, and a technology level of {self.tech_level}"

class CelestialBody():
    """ Represents a celestial body that belongs to a (star) System """
    def __init__(self, name: str, star: System):
        self.name = name
        self.star = star
        self.economy = BodyEconomyStats(self, random.randrange(1, 10), random.randint(1, 100), random.randint(1, 3))

    def __str__(self):
        return f"{self.name} is a planet that orbits {self.star.name}"
