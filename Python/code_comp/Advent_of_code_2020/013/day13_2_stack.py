
from os import path
import time as t


def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    a %= m
    if a == 0:
        a = m
    '''
    while a > m:
        a -= m
    '''
    return (m * linear_congruence(m, -b, a) + b) // a

bus_ids = []


with open(path.join(__file__, "..", "input_e.txt")) as file:
    file_string = file.read()
    file_split = file_string.split("\n")
    bus_ids = [bus_id for bus_id in file_split[1].split(",")]
    bus_ids = [int(bus_id) if bus_id != "x" else "x" for bus_id in bus_ids]


modular_equations = []
for i, bus_id in enumerate(bus_ids):
    if bus_id == "x": continue
    modular_equations.append([bus_id, (bus_id-i)%bus_id]) # x= bus_id*n + ((bus_id-i)%bus_id)

current_equation = modular_equations[0]

for equation in modular_equations[1:]:
    eq_copy = list(equation)
    eq_copy[1] = (eq_copy[1] - current_equation[1]) % eq_copy[0]
    eq_copy[1] = linear_congruence(current_equation[0], eq_copy[1], eq_copy[0])

    new_multiplier = current_equation[0] * eq_copy[0]
    new_add_constant = (eq_copy[1] * current_equation[0] + current_equation[1]) % new_multiplier

    current_equation = [new_multiplier, new_add_constant]

print(current_equation)