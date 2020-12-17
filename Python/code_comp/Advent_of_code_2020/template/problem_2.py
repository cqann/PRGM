from os import path

data = []

with open(path.join(__file__, "..", "example.txt")) as file:
    for line in file:
        data.append(line)
