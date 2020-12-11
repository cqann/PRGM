data = []

with open("day9_e.txt") as serial_file:
    data = [int(line.strip()) for line in serial_file]

preamble_length = 25

preamble = data[:preamble_length]
numbers = data[preamble_length:]
invalid_number = None

for i, number in enumerate(numbers):
    window = data[i:i+preamble_length]

    combos = set()
    for j, n1 in enumerate(window):
        for k, n2 in enumerate(window):
            if k == j: continue
            combos.add(n1 + n2)

    if number not in combos:
        invalid_number = number
        break

if invalid_number:
    for l in range(2, len(data)):
        for x in range(len(data) - l):
            window = data[x:x+l]
            if sum(window) == invalid_number:
                print(max(window) + min(window))
