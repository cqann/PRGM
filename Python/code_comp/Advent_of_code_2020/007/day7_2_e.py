import re

bag_string = ""
bag_hash = {}

with open("day7_e.txt") as bag_file:
    expression = re.compile(r"(\b\w*\b)\s(\b\w*\b)\sbag|(\d)\s(\b\w*\b)\s(\b\w*\b)\sbag", flags=re.MULTILINE|re.IGNORECASE)

    for line in bag_file:
        bag_finds = re.findall(expression, line)
        bag_key = "_".join(bag_finds.pop(0))[:-3]

        bag_hash[bag_key] = []
        for bag in bag_finds:
            bag_list = list(bag)[2:]
            if bag_list[0] == "":
                continue

            bag_hash[bag_key].append((int(bag_list.pop(0)), "_".join(bag_list)))



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


def bags_in_bag(bag_name):
    if not bag_hash[bag_name]:
        return 0

    count = 0

    for bag in bag_hash[bag_name]:
        count += bag[0] * (1 + bags_in_bag(bag[1]))

    return count

print(bags_in_bag("shiny_gold"))