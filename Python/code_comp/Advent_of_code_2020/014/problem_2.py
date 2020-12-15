from os import path
import re

data = []
mask_hash = {}

def get_possible_binaries(bin_string):
    bin_list = list(bin_string)
    index_of_first_x = "".join(bin_list).find("X")

    if index_of_first_x == -1:
        return [bin_list]
    else:
        result = []
        bin_list[index_of_first_x] = "0"
        bin_string_with_0 = list(bin_list)
        result += get_possible_binaries(bin_string_with_0)

        bin_list[index_of_first_x] = "1"
        bin_string_with_1 = list(bin_list)

        result += get_possible_binaries(bin_string_with_1)

        return ["".join(value) for value in result]


with open(path.join(__file__, "..", "input_c.txt")) as file:
    file_string = file.read()
    mask_split = re.split(r"mask\s=\s(.*)", file_string)
    mask_split.pop(0)

    current_mask = None
    for i, data in enumerate(mask_split):
        if i % 2 == 0:
            current_mask = data
        else:
            mask_hash[current_mask] = re.findall(r"mem\[(.*)\]\s=\s(.*)", data)

memory = {}

for mask, memory_operations in mask_hash.items():
    for memory_operation in memory_operations:
        index, value = memory_operation

        bin_index = bin(int(index))[2:].zfill(36)
        value_mask_zip = zip(bin_index, mask)

        result = []
        for original, mask_digit in value_mask_zip:
            if mask_digit == "0":
                result.append(original)
            elif mask_digit == "X":
                result.append("X")
            elif mask_digit == "1":
                result.append("1")

        result_bin_string = "".join(result)
        possible_indexes = get_possible_binaries(result_bin_string)
        for index in possible_indexes:
            memory[int(index, 2)] = value

print(sum([int(value) for value in memory.values()]))
