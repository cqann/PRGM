
from os import path
import re

op_codes = []

with open (path.join(__file__, "..", "input.txt")) as file:
    op_codes = [int(op_code) for op_code in re.findall("(\d+)", file.read())]


class SantaComputer:
    def __init__(self, codes):
        self.codes = codes
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
                op_code = self.codes[self.index]
            except IndexError:
                print("Final index reached")
                self.stop()
                break

            if op_code not in self.code_table:
                print(f"Opcode '{op_code}' not implemented yet.")
                continue
            else:
                self.code_table[op_code]()
                self.index += 4

    def stop(self):
        print("Stopping")
        self.is_running = False

    def add(self):
        number_1 = self.codes[self.index + 1]
        number_2 = self.codes[self.index + 2]
        number_3 = self.codes[self.index + 3]
        self.codes[number_3] = self.codes[number_1] + self.codes[number_2]
        print(" ")

    def multiply(self):
        number_1 = self.codes[self.index + 1]
        number_2 = self.codes[self.index + 2]
        number_3 = self.codes[self.index + 3]

        self.codes[number_3] = self.codes[number_1] * self.codes[number_2]
        print(" ")


if __name__ == "__main__":
    computer = SantaComputer(op_codes)
    computer.codes[1] = 12
    computer.codes[2] = 2
    computer.run()
    print(computer.codes[0])
