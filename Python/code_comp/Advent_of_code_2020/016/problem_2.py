from os import path
import re

data = []
ranges_data, your_ticket, other_ticket = None, None, None

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
acceptable_ranges = {}

for data_range in ranges_data:
    finds = re.findall(r"(\d+)-(\d+)", data_range)
    ranges = [range(int(a), int(b) + 1) for a, b in finds]
    range_name = re.findall(r"(.*):\s", data_range)[0]
    acceptable_ranges[range_name] = set()

    for singular_range in ranges:
        for i in singular_range:
            acceptable_values.add(i)
            acceptable_ranges[range_name].add(i)

valid_tickets = []

for ticket in other_tickets[1:]:
    ticket_values = [int(x) for x in ticket.split(",")]
    invalid = False
    for ticket_value in ticket_values:
        if ticket_value not in acceptable_values:
            invalid = True
            break
    if not invalid:
        valid_tickets.append(ticket_values)

your_int_ticket = [int(x) for x in your_ticket[1].split(",")]
valid_tickets.append(your_int_ticket)

columns = [[] for x in range(len(valid_tickets[0]))]
for ticket in valid_tickets:
    for i, ticket_value in enumerate(ticket):
        columns[i].append(ticket_value)


name_x_column = {}
while len(name_x_column) != len(acceptable_ranges):
    ranges_to_remove = []
    columns_to_remove = []

    for range_name, range_set in acceptable_ranges.items():
        if not range_set:
            continue

        valid_list = []

        for i, column in enumerate(columns):
            if not column:
                continue

            valid = True
            for column_value in column:
                if column_value not in range_set:
                    valid  = False
                    break
            if valid:
                valid_list.append(i)

        if len(valid_list) == 1:
            single_column = valid_list[0]

            name_x_column[range_name] = single_column
            ranges_to_remove.append(range_name)
            columns_to_remove.append(single_column)

    for range_name in ranges_to_remove:
        acceptable_ranges[range_name] = None

    for column_index in columns_to_remove:
        columns[column_index] = None

result = 1
for range_name, column_index in name_x_column.items():
    if "departure" in range_name:
        result *= your_int_ticket[column_index]

print(result)
