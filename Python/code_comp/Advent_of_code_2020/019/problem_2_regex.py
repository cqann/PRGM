from os import path
import re

messages = []
crude_rules = {}

with open(path.join(__file__, "..", "input_e.txt")) as file:
    file_string = file.read()

    finds = re.findall(r"(\d+):\s(.*)", file_string)

    for find in finds:
        key, rule = find
        crude_rules[int(key)] = rule

    crude_rules[8] = "42 | 42 8"
    crude_rules[11] = "42 31 | 42 11 31"

    messages = re.findall(r"^(\w+)$", file_string, flags=re.MULTILINE)

rules = {}

for key, crude_rule in crude_rules.items():
    or_split = crude_rule.split(" | ")

    if len(or_split) >= 2:
        rules[key] = [[int(x) for x in rule.split(" ")] for rule in or_split]
    else:
        try:
            first_number = int(crude_rule[0])
            rules[key] = [[int(x) for x in crude_rule.split(" ")]]
        except ValueError:
            rules[key] = [crude_rule[1:-1]]


regex_rules = {}

def get_rules(key):
    if key in regex_rules:
        return regex_rules[key]

    regex_rules[key] = r""

    if key == 11:
        rule_42 = get_rules(42)
        rule_31 = get_rules(31)

        regex_rules[key] = r"(" + rule_42 + rule_31 + r")"

        for i in range(2, 10):
            regex_rules[key] += r"|(" + rule_42 + r"){" + str(i) + r"}(" + rule_31 + r"){" + str(i) + r"}"
        regex_rules[key] = r"(" + regex_rules[key] + r")"
        return regex_rules[key]

    elif key == 8:
        rule_42 = get_rules(42)
        regex_rules[key] += r"((" + rule_42 + r")*)"
        return regex_rules[key]

    for i, rule in enumerate(rules[key]):
        if isinstance(rule, str):
            regex_rules[key] = rule
            break

        for rule_key in rule:
            for part in get_rules(rule_key):
                regex_rules[key] += part

        if i != len(rules[key]) - 1:
            regex_rules[key] += r"|"

    regex_rules[key] = r"(" + regex_rules[key] + r")" + r"{1}"
    return regex_rules[key]

regex_pattern = get_rules(0)

# for key in sorted(regex_rules.keys()):
    # print(key, ":", regex_rules[key])

regex_pattern = r"^" + regex_pattern + r"$"

# print(0, ":", regex_rules[0])

compiled_pattern = re.compile(regex_pattern, flags=re.MULTILINE|re.IGNORECASE)
valid = 0
for message in messages:
    match = re.match(compiled_pattern, message)
    # print(message, "YES" if match else "NO")

    if match:
        valid += 1

print(valid)

