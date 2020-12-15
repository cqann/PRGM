from os import path

orbit_hash = {}

with open (path.join(__file__, "..", "input.txt")) as file:
    for line in file:
        data = line.strip().split(")")
        key, value = tuple(reversed(data))

        if key not in orbit_hash:
            orbit_hash[key] = []
        orbit_hash[key].append(value)

def planets_orbiting(key):
    if key not in orbit_hash:
        return

    all_planets = set()

    planets = orbit_hash[key]
    all_planets.update(planets)

    for planet in planets:
        new_planets = planets_orbiting(planet)
        if new_planets:
            all_planets.update(new_planets)

    return all_planets

my_planets = planets_orbiting("YOU")
santas_planets = planets_orbiting("SAN")
connection = set.union(my_planets, santas_planets) - (my_planets&santas_planets)
print(len(connection))