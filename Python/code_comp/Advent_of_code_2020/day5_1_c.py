highest = 0
for seat in open("day5_c.txt","r"):
    seat = seat.strip()
    row = seat[:7]
    column = seat[7:]
    binary_conversion = {"F": "0", "B": "1", "R": "1", "L": "0"}
    row_binary = "".join([binary_conversion[x] for x in row])
    column_binary = "".join([binary_conversion[x] for x in column])

    row_value = int(row_binary, 2)
    column_value = int(column_binary, 2)

    seat_id = row_value * 8 + column_value
    if seat_id > highest: highest = seat_id

print(highest)