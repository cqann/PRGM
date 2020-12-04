
import re

passports = []

with open("day4_c.txt") as passport_file:
    file_string = passport_file.read()

    entries = re.split(r"^\s*$", file_string, flags=re.MULTILINE|re.IGNORECASE)

    for entry in entries:
        tmp_passport = re.split(r"\s", entry, flags=re.MULTILINE|re.IGNORECASE)
        tmp_passport = list(filter(None, tmp_passport))
        passport = {}

        for passport_key_value in tmp_passport:
            key, value = passport_key_value.split(":")
            passport[key] = value

        passports.append(passport)

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_passports = 0

for passport in passports:
    contains_all_keys = True

    for key in keys:
        if key not in passport:
            contains_all_keys = False
            break

    if contains_all_keys:
        # Check birth year
        birth_year = int(passport["byr"])
        if birth_year < 1920 or birth_year > 2002:
            continue

        # Check issue year
        issue_year = int(passport["iyr"])
        if issue_year < 2010 or issue_year > 2020:
            continue

        # Check expiration year
        expiration_year = int(passport["eyr"])
        if expiration_year < 2020 or expiration_year > 2030:
            continue

        # Check height
        height = 0
        if "cm" in passport["hgt"]:
            height = int(passport["hgt"].split("cm")[0])
            if height < 150 or height > 193:
                continue
        elif "in" in passport["hgt"]:
            height = int(passport["hgt"].split("in")[0])
            if height < 59 or height > 76:
                continue
        else:
            continue

        # Check hair color format
        hair_color = passport["hcl"]
        if hair_color[0] != "#" or len(hair_color) != 7:
            continue

        # Check eye color
        eye_color = passport["ecl"]
        if eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        # Check passport id
        passport_id = passport["pid"]
        if len(passport_id) != 9:
            continue

        valid_passports += 1

print(valid_passports)
