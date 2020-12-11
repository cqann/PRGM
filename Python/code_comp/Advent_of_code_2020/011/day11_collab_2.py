seat_map = []

with open("day11_c.txt") as seating_file:
    seat_map = [list(line.strip()) for line in seating_file]


row_length = len(seat_map[0])

OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."
generation = 0

def number_of_occupied_around(x, y, seat_map):
    number_of_occupied = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dy == 0 and dx == 0:
                continue

            n = 1
            stop_loop = False
            while not stop_loop:
                new_y = y + dy * n
                new_x = x + dx * n

                if new_y < 0 or new_x < 0:
                    break

                try:
                    if seat_map[new_y][new_x] == OCCUPIED:
                        number_of_occupied += 1
                        stop_loop = True
                    elif seat_map[new_y][new_x] == EMPTY:
                        stop_loop = True
                except IndexError:
                    stop_loop = True
                n += 1

    return number_of_occupied

while True:
    change_counter = 0
    new_map = [list(a) for a in seat_map]

    for y, row in enumerate(seat_map):
        for x, seat in enumerate(row):
            adjacent_occupied = number_of_occupied_around(x, y, seat_map)
            if seat == OCCUPIED and adjacent_occupied >= 5:
                new_map[y][x] = EMPTY
                change_counter += 1
            elif seat == EMPTY and adjacent_occupied == 0:
                new_map[y][x] = OCCUPIED
                change_counter += 1

    seat_map = new_map
    generation += 1

    if change_counter == 0:
        break

occupied_count = 0


for row in seat_map:
    occupied_count += row.count(OCCUPIED)

print(occupied_count)
