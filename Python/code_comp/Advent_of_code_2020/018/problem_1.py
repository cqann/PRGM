from os import path
import re

data = []
MULTIPLY = "*"
ADD = "+"
result = 0

def evaluate(line : str):
    parentheses = re.findall(r"\([^()\"]*(?:\"[^\"]*\"[^()\"]*)*\)", line)

    if not parentheses:
        value = different_eval(line.split(" "))
        return value

    for group in parentheses:
        value = str(different_eval(group[1:-1].split(" ")))
        line = line.replace(group, value)

    return evaluate(line)

def different_eval(tokens):
    current_result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operation, number = tokens[i:i+2]
        if operation == ADD:
            current_result += int(number)
        elif operation == MULTIPLY:
            current_result *= int(number)
        else:
            raise NotImplementedError(f"'{operation}' not implemented.")

    return current_result

with open(path.join(__file__, "..", "input_c.txt")) as file:
    for line in file:
        data.append(evaluate(line.strip()))

print(sum(data))
