
from os import path
import math as math

bus_ids = []

with open(path.join(__file__, "..", "input_e.txt")) as file:
    file_string = file.read()
    file_split = file_string.split("\n")
    bus_ids = [bus_id for bus_id in file_split[1].split(",")]
    bus_ids = [int(bus_id) if bus_id != "x" else "x" for bus_id in bus_ids]


bus_index_id_pairs = []

for i, bus_id in enumerate(bus_ids):
    if bus_id == "x":
        continue

    bus_index_id_pairs.append((i, bus_id))

dividers = {}

for i, bus_id in bus_index_id_pairs:
    for j, other_bus_id in bus_index_id_pairs[i+1:]:
        if j - i == bus_id:
            dividers.append(bus_id)
            dividers.append(other_bus_id)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return int(abs(a*b)/gcd(a, b))

increment = dividers.pop(0)
for divider in dividers:
    increment = lcm(increment, divider)

print(increment)
current_timestamp = 100000000000000
done = False

while not done:
    foo_timestamp = current_timestamp - len(bus_ids) + 1
    for i, bus_id in bus_index_id_pairs:
        if (foo_timestamp + i) % bus_id == 0:
            if i == len(bus_ids) - 1:
                print("DONE ", foo_timestamp)
                done = True
                break
        else:
            break

    current_timestamp += increment