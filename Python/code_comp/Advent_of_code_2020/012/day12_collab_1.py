
from os import path
import re
from math import cos, sin, pi

directions = []
with open(path.join(__file__, "..", "day12_c.txt")) as file:
    file_string = file.read()
    directions = [(instruction, int(distance)) for instruction, distance in re.findall("([\D])(\d+)", file_string)]

rotation = 0 # => East
x = 0
y = 0


def north(distance):
    global y
    y += distance

def south(distance):
    global y
    y -= distance

def east(distance):
    global x
    x += distance

def west(distance):
    global x
    x -= distance

def forward(distance):
    global x, y
    x += cos(rotation*(pi/180))*distance
    y += sin(rotation*(pi/180))*distance

def left(amount):
    global rotation
    rotation += amount

def right(amount):
    global rotation
    rotation -= amount

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
    command, amount = direction
    instruction_dict[command](amount)

print(round(abs(x) + abs(y)))
