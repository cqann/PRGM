
from os import path
import re
from math import cos, sin, pi, sqrt, atan2

directions = []
with open(path.join(__file__, "..", "day12_c.txt")) as file:
    file_string = file.read().strip()
    directions = [(instruction, int(distance)) for instruction, distance in re.findall("([\D])(\d+)", file_string)]

x = 0
y = 0
dx = 10
dy = 1

def north(distance):
    global dy
    dy += distance

def south(distance):
    global dy
    dy -= distance

def east(distance):
    global dx
    dx += distance

def west(distance):
    global dx
    dx -= distance

def forward(distance):
    global x, y
    x += dx*distance
    y += dy*distance

def left(amount):
    global dx, dy
    distance_to_ship = sqrt(dx**2 + dy**2)
    rotation = atan2(dy, dx) + amount*pi/180
    dx = cos(rotation)*distance_to_ship
    dy = sin(rotation)*distance_to_ship

def right(amount):
    global dx, dy
    distance_to_ship = sqrt(dx**2 + dy**2)
    rotation = atan2(dy, dx) - amount*pi/180
    dx = cos(rotation)*distance_to_ship
    dy = sin(rotation)*distance_to_ship

instruction_dict = {
     "N": lambda distance: north(distance),
     "E": lambda distance: east(distance),
     "S": lambda distance: south(distance),
     "W": lambda distance: west(distance),
     "F": lambda distance: forward(distance),
     "L": lambda amount: left(amount),
     "R": lambda amount: right(amount),
}

for direction in directions:
    command, value = direction
    instruction_dict[command](value)

print(round(abs(x) + abs(y)))
