
jump = (1, 3)

coordinates = []

with open("day3_e.txt") as map_file:
    for row in map_file:
        coordinates.append(row.strip())

    y = 0
    x = 0
    trees = 0
    while y < len(coordinates):
        if coordinates[y][x%len(coordinates[y])] == "#":
            trees += 1

        y += jump[0]
        x += jump[1]

    print(trees)


