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

    # 42 => 9 14 | 10 1
    # 31 => 14 17 | 1 13
    # 11 => 42 31
    # 11 = "42 31 | 42 11 31"
    n = 4
    for i in range(2, n):
        crude_rules[ 8] += f" |{i*' 42'}"
        crude_rules[11] += f" |{i*' 42'}{i*' 31'}"

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


word_rules = {}

def create_words_from_rule_key(rule_key):
    if rule_key in word_rules:
        return word_rules[rule_key]

    current_rules = rules[rule_key]
    rule_strings = set()

    for rule in current_rules:
        if isinstance(rule, str):
            rule_strings.add(current_rules[0])
            break

        current_rule_strings = list(create_words_from_rule_key(rule[0]))

        for i in range(1, len(rule)):
            rule1_strings = create_words_from_rule_key(rule[i])
            new_window = []

            for element1 in current_rule_strings:
                for element2 in rule1_strings:
                    word = element1 + element2
                    new_window.append(word)

            current_rule_strings = new_window

        for word in current_rule_strings:
            rule_strings.add(word)

    word_rules[rule_key] = rule_strings
    return rule_strings

create_words_from_rule_key(0)
possible_words = word_rules[0]
# print(word_rules)

result = 0
for message in messages:
    if message in possible_words:
        result += 1

print(result)
