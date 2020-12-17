from os import path

starting_numbers = []

with open(path.join(__file__, "..", "input_e.txt")) as file:
    starting_numbers = [int(n) for n in file.read().strip().split(",")]

ages = {number: time + 1 for time, number in enumerate(starting_numbers)}
last_number = starting_numbers[-1]

current_number = last_number
for i in range(len(starting_numbers), 30000000):
    if current_number in ages:
        last_time_said = ages[current_number]
        ages[current_number] = i
        current_number = i - last_time_said
    else:
        ages[current_number] = i
        current_number = 0

print(current_number)