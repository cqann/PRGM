
import re

commands = []

with open("day8_c.txt") as bootcode_file:
    string_file = bootcode_file.read()
    commands = [(x[0], int(x[1])) for x in re.findall("(\w+)\s((\+|\-)\d+)", string_file)]

visited = [False] * len(commands)
index = 0
accumulator = 0

def jmp(operation):
    global index
    index += operation

def nop():
    global index
    index += 1

def acc(operation):
    global index, accumulator
    accumulator += operation
    index += 1

instructions = {
    "jmp": lambda *args: jmp(*args),
    "acc": lambda *args: acc(*args),
    "nop": lambda *args: nop(*args),
}

while True:
    if visited[index]:
        break
    else:
        visited[index] = True

    instruction, operation = commands[index]
    instructions[instruction](operation)

print(accumulator)
