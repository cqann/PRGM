from os import path
import re

data = []
ranges_data = None
your_ticket = None
other_ticket = None

with open(path.join(__file__, "..", "input_e.txt")) as file:
    data = [[]]

    for line in file:
        line = line.strip()
        if line:
            data[-1].append(line)
        else:
            data.append([])

    ranges_data, your_ticket, other_tickets = data

acceptable_values = set()
for data_range in ranges_data:
    finds = re.findall(r"(\d+)-(\d+)", data_range)
    ranges = [range(int(a), int(b) + 1) for a, b in finds]

    for singular_range in ranges:
        for i in singular_range:
            acceptable_values.add(i)

error_count = 0
for ticket in other_tickets[1:]:
    ticket_values = [int(x) for x in ticket.split(",")]

    for ticket_value in ticket_values:
        if ticket_value not in acceptable_values:
            error_count += ticket_value

print(error_count)
