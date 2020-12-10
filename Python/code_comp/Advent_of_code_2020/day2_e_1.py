
import re

with open("day2_e.txt") as password_file:
    password_string = password_file.read()
    finds = re.findall("(\d+)-(\d+)\s(\w+):\s(\w+)", password_string)

    valid_passwords = 0
    print(finds)

    for password_rules in finds:
        minimum, maximum, letter, password = password_rules

        if list(password).count(letter) in range(int(minimum), int(maximum) + 1):
            valid_passwords += 1

    print(valid_passwords)

