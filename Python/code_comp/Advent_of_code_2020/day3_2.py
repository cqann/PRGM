
file = open("day3.txt", "r")

hill_map = [[y for y in list(x[:-1])] for x in file]

finish_line = len(hill_map)
edge = len(hill_map[0])
to_check = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1
for d in to_check:
    dy = d[1]
    dx = d[0]
    y = 0
    x = 0
    tree_count = 0

    while y < finish_line:
        if hill_map[y][x] == "#":
            tree_count += 1

        y += dy
        x += dx
        x %= edge

    result *= tree_count

print(result)