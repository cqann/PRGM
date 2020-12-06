def determine_valid(passport):
    pass_len = len(passport.keys())
    required = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
    key_count = 0
    for key in passport:
        if key in required:
            key_count += 1
    if key_count >= 7:
        return 1
    else:
        return 0

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
