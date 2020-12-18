
from os import path
import random

initial_memory = {}

with open (path.join(__file__, "..", "input.txt")) as file:
    initial_memory = {str(i): op_code for i, op_code in enumerate(file.read().split(","))}


class SantaComputer:
    NO_INCREMENT = 1
    HALT = 2

    def __init__(self, initial_memory):
        self.memory = initial_memory
        self.initial_memory = initial_memory
        self.is_running = False
        self.index = 0
        self.relative_base = 0

        # op_code: (function, number of parameters required)
        self.code_table = {
            99: (self.stop, 0),
            1: (self.add, 3),
            2: (self.multiply, 3),
            3: (self.input, 1),
            4: (self.output, 1),
            5: (self.jump_if_true, 2),
            6: (self.jump_if_false, 2),
            7: (self.less_than, 3),
            8: (self.equals, 3),
            9: (self.change_base, 1),
        }

    def run(self):
        self.is_running = True
        while(self.is_running):
            value = str(self.get(self.index))

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

            return_code = self.code_table[op_code][0](*parameter_indexes)

            if return_code == self.NO_INCREMENT:
                continue
            elif return_code == self.HALT:
                break

            self.index += number_of_parameters + 1
            self.update()

    def update(self):
        pass

    def set_pointer(self, new_index):
        self.index = int(new_index)

    def get_parameter_index(self, index, mode):
        parameter_index = -1
        if mode == 0:
            parameter_index = self.get(index)
        elif mode == 1:
            parameter_index = index
        elif mode == 2:
            parameter_index = self.relative_base + int(self.get(index))
        else:
            raise NotImplementedError(f"Parameter mode '{mode}' not implemented yet.")

        return parameter_index

    def reset(self):
        self.memory = {key: value for key, value in self.initial_memory.items()}
        self.index = 0

    def stop(self):
        self.is_running = False
        return self.HALT

    def change_base(self, index1):
        self.relative_base += int(self.get(index1))

    def input(self, index1):
        data = input("Input: ")
        self.set(index1, data)

    def output(self, index1):
        print(self.get(index1))

    def jump_if_true(self, index1, index2):
        number1 = str(self.get(index1))
        if number1 != "0":
            self.set_pointer(self.get(index2))
            return self.NO_INCREMENT

    def jump_if_false(self, index1, index2):
        number1 = str(self.get(index1))
        if number1 == "0":
            self.set_pointer(self.get(index2))
            return self.NO_INCREMENT

    def equals(self, index1, index2, index3):
        number1 = int(self.get(index1))
        number2 = int(self.get(index2))
        if number1 == number2:
            self.set(index3, 1)
        else:
            self.set(index3, 0)

    def less_than(self, index1, index2, index3):
        number1 = int(self.get(index1))
        number2 = int(self.get(index2))
        if number1 < number2:
            self.set(index3, 1)
        else:
            self.set(index3, 0)

    def add(self, index1, index2, index3):
        number1 = int(self.get(index1))
        number2 = int(self.get(index2))
        self.set(index3, number1 + number2)

    def multiply(self, index1, index2, index3):
        number1 = int(self.get(index1))
        number2 = int(self.get(index2))
        self.set(index3, number1 * number2)

    def get(self, index):
        index = str(index)
        if index not in self.memory:
            self.memory[index] = str(0)

        return self.memory[index]

    def set(self, index, value):
        self.memory[str(index)] = str(value)


class SantaRepairBot(SantaComputer):
    def __init__(self, initial_memory):
        super().__init__(initial_memory)
        self.grid = {(0, 0): 0}
        self.x = 0
        self.y = 0
        self.status = 0
        self.tile_sheet = {
            0: "  ", # Empty
            1: "##", # Wall
            2: "<>", # Droid
            3: "..", # Floor
            4: "OO", # Oxygen Tank
            5: "SS", # START
        }
        self.directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        self.direction_index_to_computer_input = [
            1,
            4,
            2,
            3,
        ]
        self.direction_index = 0
        self.n = 0

    def draw_grid(self):
        coordinates = computer.grid.keys()
        min_x = min(coordinates, key = lambda coordinate: coordinate[0])[0]-1
        min_y = min(coordinates, key = lambda coordinate: coordinate[1])[1]-1

        max_x = max(coordinates, key = lambda coordinate: coordinate[0])[0]+2
        max_y = max(coordinates, key = lambda coordinate: coordinate[1])[1]+2

        grid = []
        turtle_pos = (self.x, self.y)

        for y in range(min_y, max_y):
            line = ""
            for x in range(min_x, max_x):
                coord = (x, y)

                if coord == turtle_pos:
                    line += self.tile_sheet[2]
                    continue

                if coord == (0, 0):
                    line += self.tile_sheet[5]
                    continue

                if coord not in self.grid:
                    line += self.tile_sheet[0]
                else:
                    line += self.tile_sheet[self.grid[coord]]
            grid.append(line)

        for line in reversed(grid):
            print(line)
        print()

    def input(self, index1):
        self.direction_index %= len(self.directions)
        self.set(index1, self.direction_index_to_computer_input[self.direction_index])
        self.n += 1

        if self.n % 10000 == 0:
            # self.draw_grid()
            pass

    def update_grid_according_to_status(self):
        dx, dy = self.directions[self.direction_index]

        if self.status == 0:
            self.grid[(self.x + dx, self.y + dy)] = 1
        elif self.status >= 1:
            self.x += dx
            self.y += dy
            self.grid[(self.x, self.y)] = self.status + 2

        # if self.status == 2:
        #     self.stop()

        if self.n % 900000 == 0:
            self.stop()

    def manual_control(self):
        next_move = ""

        movement_map = {
            "w": 4,
            "s": 2,
            "a": 3,
            "d": 1
        }

        while next_move not in movement_map:
            next_move = input("").lower()

        self.direction_index = movement_map[next_move]

    def random_direction(self):
        self.direction_index = random.randint(1, 4)

    def get_position(self, x, y):
        position = (x, y)
        if position not in self.grid:
            return None

        return self.grid[position]

    def calculate_next_move(self):
        dx, dy = self.directions[(self.direction_index + 1)%len(self.directions)]
        tile_to_right = self.get_position(self.x + dx, self.y + dy)

        ok_good_bois = [None, 3, 0]

        if tile_to_right in ok_good_bois:
            self.direction_index += 1
            return

        self.direction_index -= 1
        dx, dy = self.directions[(self.direction_index + 1)%len(self.directions)]
        tile_in_front = self.get_position(self.x + dx, self.y + dy)

        if tile_in_front in ok_good_bois:
            return

    probing = True
    returning = False
    probe_ditrection = 0

    def output(self, index1):
        number = int(self.get(index1))
        self.status = number
        self.update_grid_according_to_status()
        self.random_direction()

if __name__ == "__main__":
    computer = SantaRepairBot(initial_memory)
    computer.run()
    computer.draw_grid()
    print(computer.grid)


