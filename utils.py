import random

def get_star_names():
    with open("data/name_star.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

def get_planet_names():
    with open("data/name_location.txt", "r") as location_file, open("data/name_adjectives.txt", "r") as adj_file:
        
        locations = random.choice([line.strip() for line in location_file.readlines()])
        adjectives = random.choice([line.strip() for line in adj_file.readlines()])
        return f"{adjectives} {locations}"
    
def get_adjective_names():
    with open("data/name_adjectives.txt", "r") as file:
        return [line.strip() for line in file.readlines()]