
import re
from os import path

initial_timestamp = 0
bus_ids = []

with open(path.join(__file__, "..", "input_c.txt")) as file:
    file_string = file.read()
    file_split = file_string.split("\n")
    initial_timestamp = int(file_split[0])
    bus_ids = list(map(int, re.findall("(\d+)", file_split[1])))

current_timestamp = initial_timestamp
done = False

while not done:
    for bus_id in bus_ids:
        if current_timestamp % bus_id == 0:
            print(bus_id * (current_timestamp - initial_timestamp))
            done = True
            break

    current_timestamp += 1
