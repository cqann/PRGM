from os import path

orbit_hash = {}

with open (path.join(__file__, "..", "input.txt")) as file:
    for line in file:
        data = line.strip().split(")")
        key, value = tuple(data)

        if key not in orbit_hash:
            orbit_hash[key] = []
        orbit_hash[key].append(value)

def number_of_orbits(key):
    if key not in orbit_hash:
        return 0

    planets = orbit_hash[key]
    orbits = len(planets)

    for planet in planets:
        orbits += number_of_orbits(planet)

    return orbits

print(sum([number_of_orbits(key) for key in orbit_hash.keys()]))