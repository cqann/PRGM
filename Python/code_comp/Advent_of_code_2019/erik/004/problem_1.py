
import re

input1 = 357253
input2 = 892942
input_range = range(input1, input2+1)

possible_passwords = list(map(list, map(str, input_range)))
correct_passwords = set()

for password in possible_passwords:
    password_string = "".join(password)
    correct = False
    finds = re.finditer(r"(\d)\1+", password_string)

    for match in finds:
        if len(match.group(0)) == 2:
            correct = True

    if not correct:
        continue

    previous_digit = password.pop(0)

    for digit in password:
        if int(digit) < int(previous_digit):
            correct = False
            break
        previous_digit = digit

    if correct:
        correct_passwords.add(password_string)

print(len(correct_passwords))
