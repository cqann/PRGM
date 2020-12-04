
import re

passports = []

with open("day4_e.txt") as passport_file:
    file_string = passport_file.read()

    entries = re.split(r"^\s*$", file_string, flags=re.MULTILINE|re.IGNORECASE)

    for entry in entries:
        passport = "".join(re.split(r"\s", entry, flags=re.MULTILINE|re.IGNORECASE))
        print(passport)
        passports.append(passport)

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_passports = 0

for passport in passports:
    valid = True
    for key in keys:
        if key not in passport:
            valid = False

    if valid:
        valid_passports += 1

print(valid_passports)
