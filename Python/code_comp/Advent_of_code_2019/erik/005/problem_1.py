
import enum
from os import path
import re

initial_memory = []

with open (path.join(__file__, "..", "input.txt")) as file:
    initial_memory = [op_code for op_code in re.findall("(\d+)", file.read())]


class SantaComputer:
    def __init__(self, initial_memory):
        self.memory = initial_memory
        self.initial_memory = list(initial_memory)
        self.is_running = False
        self.index = 0

        # op_code: (function, number of parameters required)
        self.code_table = {
            99: (self.stop, 0),
            1: (self.add, 3),
            2: (self.multiply, 3),
            3: (self.input, 1),
            4: (self.output, 1)
        }

    def run(self):
        self.is_running = True
        while(self.is_running):
            try:
                value = str(self.get(self.index))
            except IndexError:
                self.stop()
                break

            op_code = int(value[-2:]) # last two digits
            if op_code not in self.code_table:
                raise NotImplementedError(f"Opcode '{op_code}' not implemented yet.")

            number_of_parameters = self.code_table[op_code][1]
            zero_filled_value = value.rjust(number_of_parameters + 2, "0")
            parameter_modes = list(reversed(zero_filled_value[:-2])) # everything except last two
            parameter_indexes = []
            for i in range(number_of_parameters):
                mode = parameter_modes[i] if i < len(parameter_modes) else 0
                parameter_indexes.append(self.get_parameter_index(self.index + i + 1, int(mode)))

            self.code_table[op_code][0](*parameter_indexes)
            self.index += number_of_parameters + 1

    def get_parameter_index(self, index, mode):
        parameter_index = -1
        if mode == 0:
            parameter_index = self.get(index)
        elif mode == 1:
            parameter_index = index
        else:
            raise NotImplementedError(f"Parameter mode '{mode}' not implemented yet.")

        return parameter_index

    def reset(self):
        self.memory = list(self.initial_memory)
        self.index = 0

    def stop(self):
        self.is_running = False

    def input(self, index1):
        data = input()
        self.set(self.get(index1), data)

    def output(self, index1):
        print(self.get(index1))

    def add(self, index1, index2, index3):
        self.set(index3, int(self.get(index1)) + int(self.get(index2)))

    def multiply(self, index1, index2, index3):
        self.set(index3, int(self.get(index1)) * int(self.get(index2)))

    def get(self, index):
        return  self.memory[int(index)]

    def set(self, index, value):
        index = int(index)
        if index == len(self.memory):
            self.memory.append(value)
        else:
            self.memory[int(index)] = str(value)


if __name__ == "__main__":
    computer = SantaComputer(initial_memory)
    computer.run()
