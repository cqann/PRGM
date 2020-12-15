
from os import path
import time as t


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

bus_ids = []


with open(path.join(__file__, "..", "input_c.txt")) as file:
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
    while gcd(current_equation[0],eq_copy[0]) != 1:
        current_equation[0] = (current_equation[0] - eq_copy[0]) % eq_copy[0]
    while eq_copy[1] / current_equation[0] != int(eq_copy[1] / current_equation[0]):
        eq_copy[1] += eq_copy[0]
    eq_copy[1] /= current_equation[0]


    new_multiplier = current_equation[0] * eq_copy[0] 
    new_add_constant = (eq_copy[1] * current_equation[0] + current_equation[1]) % new_multiplier
    
    current_equation = [new_multiplier, new_add_constant]

print(int(current_equation[1]))