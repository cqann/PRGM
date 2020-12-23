from os import path
import re
from itertools import combinations, permutations, product

messages = []
crude_rules = {}

with open(path.join(__file__, "..", "input_c.txt")) as file:
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
    if len(or_split) == 2:
        rule1, rule2 = [[int(x) for x in rule.split(" ")] for rule in or_split]
        rules[key] = [rule1, rule2]
    else:
        try:
            first_number = int(crude_rule[0])
            rules[key] = [[int(x) for x in crude_rule.split(" ")]]
        except ValueError:
            rules[key] = [crude_rule[1:-1]]

word_rules = {}

def create_words_from_rule_key(rule_key, n = 0):
    if rule_key in word_rules:
        return word_rules[rule_key]

    current_rules = rules[rule_key]
    rule_strings = set()

    for rule in current_rules:
        if isinstance(rule, str):
            rule_strings.add(current_rules[0])
            break

        current_rule_strings = list(create_words_from_rule_key(rule[0], n))

        for i in range(1, len(rule)):
            rule1_strings = create_words_from_rule_key(rule[i], n)
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

create_words_from_rule_key(42)
create_words_from_rule_key(31)
rule_42 = word_rules[42]
rule_31 = word_rules[31]
word_length = 0
for word in rule_42: 
    word_length = len(word)

result = 0
for message in messages:
    if len(message)%word_length != 0:
        continue

    fits_pattern = True 
    rev_message = "".join(reversed(message))
    divisions = len(message)  // word_length
    if divisions < 3: 
        continue
    rule_11_count = 0

    for i in range(divisions):
        real_i = i * word_length
        rev_division = rev_message[real_i:real_i+word_length]
        division = "".join(reversed(rev_division))
        if division in rule_31:
            rule_11_count += 1
        else:
            break 
        if i == divisions - 1:
            fits_pattern = False
    
    rule_11_count *= 2
    if not fits_pattern or rule_11_count in [0, divisions]:
        continue
    remaining_message = message[0 : len(message) - rule_11_count * word_length]

    divisions = len(remaining_message) // word_length
    for i in range(divisions):
        i *= word_length
        division = message[i:i+word_length]

        if division not in rule_42:
            fits_pattern = False
            break
    
    if fits_pattern:
        result += 1

print(result)
    


