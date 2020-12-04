
file = open("day3.txt", "r")

hill_map = [[y for y in list(x[:-1])] for x in file]

finish_line = len(hill_map)
edge = len(hill_map[0])
y = 0
x = 0
tree_count = 0

while y < finish_line:
    if hill_map[y][x] == "#":
        tree_count += 1

    y += 1
    x += 3
    x %= edge

print(tree_count)