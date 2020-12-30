from os import path
import re

tiles = {}

with open(path.join(__file__, "..", "input_c.txt")) as file:
    file_text = file.read()
    raw_tiles = re.split(r"Tile (\d+):", file_text, flags=re.MULTILINE)[1:]
    tile_dic = {}

    tiles = {tile_id: [x for x in value.split("\n") if x != ""] for tile_id, value in re.findall(r"Tile (\d+):\s([.#\n]*)", file_text)}

tile_info = {}

for tile_id, rows in tiles.items():
    current_info = {}
    current_info["up"] = rows[0]
    current_info["down"] = rows[-1]

    current_info["left"] = "".join([row[0] for row in rows])
    current_info["right"] = "".join([row[-1] for row in rows])

    current_rev_x = dict(current_info)
    current_rev_x["up"] = "".join(list(reversed(current_rev_x["up"])))
    current_rev_x["down"] = "".join(list(reversed(current_rev_x["down"])))

    current_rev_y = dict(current_info)
    current_rev_y["right"] = "".join(list(reversed(current_rev_y["right"])))
    current_rev_y["left"] = "".join(list(reversed(current_rev_y["left"])))

    tile_info[tile_id] = (current_info, current_rev_x, current_rev_y)

def find_neighbour(tile_id_1, side_1):
    count = [0,0,0]
    for tile_id_2, info_2 in tile_info.items():
        if tile_id_1 == tile_id_2:
            continue

        for i, state in enumerate(info_2):
            for side_2 in state.values():
                if side_1 == side_2:
                    count[i] += 1
    return max(count)


shared_border_counts = {}
for tile_id_1, info_1 in tile_info.items():
    shared_border_count = [0,0,0]
    for i, state in enumerate(info_1):
        rotations = state.values()
        for side_1 in rotations:
            shared_border_count[i] += find_neighbour(tile_id_1, side_1)

    shared_border_counts[tile_id_1] = shared_border_count

corner_ids = []
for tile_id, shared_border_count in shared_border_counts.items():
    max_val = max(shared_border_count)
    if max_val == 2:
        corner_ids.append(int(tile_id))

result = 1
for corner_id in corner_ids:
    result *= corner_id

print(result)