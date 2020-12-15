
from os import path
import re

initial_memory = []

with open (path.join(__file__, "..", "input.txt")) as file:
    initial_memory = [int(op_code) for op_code in re.findall("(\d+)", file.read())]


class SantaComputer:
    def __init__(self, initial_memory):
        self.memory = initial_memory
        self.initial_memory = list(initial_memory)
        self.is_running = False
        self.index = 0
        self.code_table = {
            99: self.stop,
            1: self.add,
            2: self.multiply
        }

    def run(self):
        self.is_running = True
        while(self.is_running):
            try:
                op_code = self.memory[self.index]
            except IndexError:
                self.stop()
                break

            if op_code not in self.code_table:
                print(f"Opcode '{op_code}' not implemented yet.")
                continue
            else:
                self.code_table[op_code]()

    def reset(self):
        self.memory = list(self.initial_memory)
        self.index = 0

    def stop(self):
        self.is_running = False
        self.index += 1

    def add(self):
        index_1 = self.get(self.index + 1)
        index_2 = self.get(self.index + 2)
        index_3 = self.get(self.index + 3)
        self.set(index_3, self.get(index_1) + self.get(index_2))
        self.index += 4

    def multiply(self):
        index_1 = self.get(self.index + 1)
        index_2 = self.get(self.index + 2)
        index_3 = self.get(self.index + 3)

        self.set(index_3, self.get(index_1) * self.get(index_2))
        self.index += 4

    def set_inputs(self, a, b):
        self.set(1, a)
        self.set(2, b)

    def get_output(self):
        return self.get(0)

    def get(self, index):
        return self.memory[index]

    def set(self, index, value):
        self.memory[index] = value


if __name__ == "__main__":
    computer = SantaComputer(initial_memory)

    for i in range(100):
        for j in range(100):
            if i == j:
                continue

            computer.reset()
            computer.set_inputs(i, j)
            computer.run()
            if computer.get_output() == 19690720:
                print(100 * i + j)
