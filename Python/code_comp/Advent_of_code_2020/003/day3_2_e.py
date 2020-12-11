
jumps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

coordinates = []

with open("day3_e.txt") as map_file:
    for row in map_file:
        coordinates.append(row.strip())


    answer = 1
    for jump in jumps:
        y = 0
        x = 0
        trees = 0
        while y < len(coordinates):
            if coordinates[y][x%len(coordinates[y])] == "#":
                trees += 1

            y += jump[0]
            x += jump[1]

        answer *= trees

    print(answer)


