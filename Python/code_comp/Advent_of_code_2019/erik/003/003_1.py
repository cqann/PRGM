
from os import path
import re

wires = []

with open (path.join(__file__, "..", "input.txt")) as file:
    for line in file:
        wires.append([(instruction, int(value)) for instruction, value in re.findall("(\D)(\d+)", line)])


x = 0
y = 0
coordinate_hash = {}

def save_coordinates(wire):
    global x, y, coordinate_hash
    if x not in coordinate_hash:
        coordinate_hash[x] = {}

    if y not in coordinate_hash[x]:
        coordinate_hash[x][y] = {}

    if wire not in coordinate_hash[x][y]:
        coordinate_hash[x][y][wire] = 0

    coordinate_hash[x][y][wire] += 1

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
for x in coordinate_hash.keys():
    for y in coordinate_hash[x].keys():
        location = coordinate_hash[x][y]
        if len(location) > 1 and x != 0 and y != 0:
            intersections.append((x, y, abs(x) + abs(y)))

distances = [distance for x, y, distance in intersections]
print(min(distances) if distances else "No Intersections")