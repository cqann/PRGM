from os import path
import re

messages = []
crude_rules = {}

with open(path.join(__file__, "..", "example.txt")) as file:
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

    for i, rule in enumerate(rules[key]):
        if isinstance(rule, str):
            regex_rules[key] = rule
            break

        for rule_key in rule:
            if rule_key == key:
                regex_rules[key] += r"(" + regex_rules[key] + r")*"
                continue

            for part in get_rules(rule_key):
                regex_rules[key] += part

        if i != len(rules[key]) - 1:
            regex_rules[key] += "|"

    regex_rules[key] = r"(" + regex_rules[key] + r")" + r"{1}"
    return regex_rules[key]

regex_pattern = get_rules(0)

for key, rule in regex_rules.items():
    print(key, ":", rule)

regex_pattern = r"^" + regex_pattern + r"$"
compiled_pattern = re.compile(regex_pattern, flags=re.MULTILINE|re.IGNORECASE)
valid = 0
for message in messages:
    match = re.match(compiled_pattern, message)
    print(message, "YES" if match else "NO")

    if match:
        valid += 1

print(valid)

