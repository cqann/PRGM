
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

def nop(operation):
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

def exits(mod_commands):
    global index, accumulator

    new_visited = [False] * len(mod_commands)
    old_index = int(index)
    old_accumulator = int(accumulator)
    result = False

    index = 0
    accumulator = 0

    while True:
        if index == len(mod_commands):
            result = True
            break
        if new_visited[index]:
            break
        else:
            new_visited[index] = True

        instruction, operation = mod_commands[index]
        instructions[instruction](operation)

    if result == True:
        print(accumulator)

    index = old_index
    accumulator = old_accumulator
    return result


while True:
    if visited[index]:
        break
    else:
        visited[index] = True

    instruction, operation = commands[index]

    if instruction == "nop":
        mod_commands = list(commands)
        mod_commands[index] = ("jmp",operation)
        if exits(mod_commands):
            print("change index ", index, " to jmp!")
            break
    elif instruction == "jmp":
        mod_commands = list(commands)
        mod_commands[index] = ("nop", operation)
        if exits(mod_commands):
            print("change index ", index, " to nop!")
            break
        else:
            visited[index] = True

    instruction, operation = commands[index]
    instructions[instruction](operation)


