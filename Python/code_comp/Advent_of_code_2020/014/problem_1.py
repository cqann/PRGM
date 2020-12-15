from os import path
import re

data = []
mask_hash = {}

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

        bin_value = bin(int(value))[2:].zfill(36)
        value_mask_zip = zip(bin_value, mask)
        result = [original if  mask_digit == "X" else mask_digit for original, mask_digit in value_mask_zip]

        result_bin_string = "".join(result)
        memory[index] = int(result_bin_string, 2)


print(sum([value for value in memory.values()]))
