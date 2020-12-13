
from os import path

bus_ids = []

with open(path.join(__file__, "..", "example.txt")) as file:
    file_string = file.read()
    file_split = file_string.split("\n")
    bus_ids = [bus_id for bus_id in file_split[1].split(",")]
    bus_ids = [int(bus_id) if bus_id != "x" else "x" for bus_id in bus_ids]


bus_id_index_pairs = {}
for i, bus_id in enumerate(bus_ids):
    if bus_id == "x": continue
    bus_id_index_pairs[bus_id] = i

current_timestamp = 0
increment = 7

# 7, 13, x, x, 59, x, 31, 19
# 0, 1,  2, 3, 4,  5, 6,  7

increment = max(bus_id_index_pairs.keys())
done = False
current_timestamp = 0

while not done:
    foo_timestamp = current_timestamp - bus_id_index_pairs[increment]
    for bus_id, i in bus_id_index_pairs.items():
        if (foo_timestamp + i) % bus_id == 0:
            if i == len(bus_ids) - 1:
                print("DONE ", foo_timestamp)
                done = True
                break
        else:
            break

    current_timestamp += increment