from os import path
from itertools import product

active = set()

with open(path.join(__file__, "..", "input_c.txt")) as file:
    z = 0
    w = 0
    for x, line in enumerate(file):
        for y, character in enumerate(line.strip()):
            if character == ".":
                continue

            active.add((x, y, z, w))


neighbours = set(product([-1, 0, 1], repeat=4))
neighbours.remove((0, 0, 0, 0))

for _ in range(6):
    potential_inactive = {}
    new_active = set()

    for coordinate in active:
        active_count = 0

        for neighbour in neighbours:
            new_coordinate = tuple(coord + neigh for coord, neigh in zip(coordinate, neighbour))

            if new_coordinate in active:
                active_count += 1
                continue

            if new_coordinate not in potential_inactive:
                potential_inactive[new_coordinate] = 0
            potential_inactive[new_coordinate] += 1

        if active_count in [2,3]:
            new_active.add(coordinate)

    for coordinate, active_count in potential_inactive.items():
        if active_count == 3:
            new_active.add(coordinate)

    active = new_active

print(len(active))