


from os import path
import re

wires = []

with open (path.join(__file__, "..", "input.txt")) as file:
    for line in file:
        wires.append([(instruction, int(value)) for instruction, value in re.findall("(\D)(\d+)", line)])


x = 0
y = 0
wire_coordinates = {}

def save_coordinates(wire):
    global x, y, coordinate_hash, wire_coordinates
    if wire not in wire_coordinates:
        wire_coordinates[wire] = []

    wire_coordinates[wire].append((x, y))

def right(d, wire):
    global x
    old_x = int(x)
    for i in range(1, d + 1):
        x = old_x + i
        save_coordinates(wire)

def up(d, wire):
    global y
    old_y = int(y)
    for i in range(1, d + 1):
        y = old_y + i
        save_coordinates(wire)

def left(d, wire):
    global x
    old_x = int(x)
    for i in range(1, d + 1):
        x = old_x - i
        save_coordinates(wire)

def down(d, wire):
    global y
    old_y = int(y)
    for i in range(1, d + 1):
        y = old_y - i
        save_coordinates(wire)


instruction_map = {
    "R": right,
    "U": up,
    "L": left,
    "D": down,
}

for i, wire in enumerate(wires):
    for instruction, distance in wire:
        instruction_map[instruction](distance, i)
    x = 0
    y = 0


intersections = []
for coordinate_1 in wire_coordinates[0]:
    if coordinate_1 in wire_coordinates[1]:
        x, y = coordinate_1
        d1 = wire_coordinates[0].index(coordinate_1)
        d2 = wire_coordinates[1].index(coordinate_1)

        intersections.append((x, y, d1 + d2 + 2))


distances = [distance for x, y, distance in intersections]
print(min(distances) if distances else "No Intersections")