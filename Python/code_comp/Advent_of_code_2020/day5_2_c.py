ids = []
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
    ids.append(seat_id)

ids.sort()

last = ids[0]
for i in ids[1:]: 
    if i != last + 1:
        print(i-1)
    last = i
    