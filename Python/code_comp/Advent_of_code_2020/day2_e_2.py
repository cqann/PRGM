
import re

with open("day2_e.txt") as password_file:
    password_string = password_file.read()
    finds = re.findall("(\d+)-(\d+)\s(\w+):\s(\w+)", password_string)

    valid_passwords = 0
    print(finds)

    for password_rules in finds:
        minimum, maximum, letter, password = password_rules

        first = password[int(minimum) - 1] == letter
        second = password[int(maximum) - 1] == letter

        if first != second:
            valid_passwords += 1

    print(valid_passwords)

