import re

def determine_valid(passport):
    rules = {
        "byr": lambda a : int(a) in range(1920, 2003),
        "iyr": lambda a : int(a) in range(2010, 2021),
        "eyr": lambda a : int(a) in range(2020, 2031),
        "hgt": lambda a : (a[-2:] in ["in","cm"]) and (int(a[:-2]) in range(150, 194) if a[-2:] == "cm" else int(a[:-2]) in range(59, 77)),
        "hcl": lambda a : bool(re.compile("^#[0-9a-f]{6}").match(a)) and len(a) == 7,
        "ecl": lambda a : a in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda a : bool(re.compile("^[0-9]{9}").match(a)) and len(a) == 9,
        "cid": lambda a : True
    }
    required = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
    key_count = 0
    for key in passport:
        if key in required: key_count += 1
        value = passport[key]
        print(key, value, rules[key](value) )
        if not rules[key](value):
            return 0 
    if key_count < 7:
        return 0
    
    return 1


file = open("day4_c.txt", "r")

passports = [{}]
valid_count = 0
for line in file:
    if line == "\n": 
        valid_count += determine_valid(passports[-1])
        passports.append({})
        continue

    for pair in line[:-1].split(" "):
        key, value = pair.split(":")
        passports[-1][key] = value
    
valid_count += determine_valid(passports[-1])

print(valid_count)
