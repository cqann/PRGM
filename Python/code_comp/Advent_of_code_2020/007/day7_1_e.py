import re

bag_string = ""
bag_hash = {}

with open("day7_e.txt") as bag_file:
    expression = re.compile(r"(\b\w*\b)\s(\b\w*\b)\sbag", flags=re.MULTILINE|re.IGNORECASE)
    for line in bag_file:
        finds = re.findall(expression, line)
        key_bag = finds.pop(0)
        bag_hash["_".join(key_bag)] = ["_".join(bag) for bag in finds]


def can_hold_gold(bag_name):
    global bag_hash

    if bag_name not in bag_hash:
        return False

    if "shiny_gold" in bag_hash[bag_name]:
        return True

    for bag in bag_hash[bag_name]:
        if can_hold_gold(bag):
            return True

    return False

bags_that_can_hold_gold = 0


for bag_name in bag_hash:
    if can_hold_gold(bag_name):
        bags_that_can_hold_gold += 1

print(bags_that_can_hold_gold)
