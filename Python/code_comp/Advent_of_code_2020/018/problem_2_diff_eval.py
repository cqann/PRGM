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
    token_string = "".join(tokens)

    while True:
        addition = re.search(r"((\d+)\+(\d+))", token_string)
        if not addition:
            break

        original_string, a, b = addition.groups()
        token_string = token_string.replace(original_string, str(int(a) + int(b)), 1)

    while True:
        multiplication = re.search(r"((\d+)\*(\d+))", token_string)
        if not multiplication:
            break

        original_string, a, b = multiplication.groups()
        token_string = token_string.replace(original_string, str(int(a) * int(b)), 1)

    return int(token_string)

with open(path.join(__file__, "..", "input_c.txt")) as file:
    for line in file:
        data.append(evaluate(line.strip()))


print(sum(data))