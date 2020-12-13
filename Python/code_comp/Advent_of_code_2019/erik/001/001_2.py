
import math as math
from os import path, getcwd

def module_fuel(mass):
    fuel = math.floor(mass/3) - 2
    if fuel < 0:
        return 0
    else:
        fuel += module_fuel(fuel)

    return fuel

with open (path.join(getcwd(), "input.txt")) as module_file:
    fuel_list = [module_fuel(int(line)) for line in module_file]

    print(sum(fuel_list))

