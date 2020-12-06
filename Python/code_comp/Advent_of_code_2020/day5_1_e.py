
data = []
import re

with open("day5_e.txt") as seat_file:

    for line in seat_file:
        new_line = line.replace("B", "1").replace("F", "0").strip()
        line_split = re.split(re.compile(r"(\D+)"), new_line)

        data.append((
            int(line_split[0], 2),
            int(line_split[1].replace("R", "1").replace("L", "0"), 2)
        ))

    ids = []
    for row, column in data:
        ids.append(row * 8 + column)

    print(max(ids))