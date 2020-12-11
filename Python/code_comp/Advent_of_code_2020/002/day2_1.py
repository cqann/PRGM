


inputs = [x[:-1] for x in open("day2.txt","r")]
valid_count = 0
for entry in inputs:
    rule, password = entry.split(":")
    limit, letter = rule.split(" ")
    password = password[1:]
    lower, upper = [int(x) for x in limit.split("-")]

    if list(password).count(letter) in range(lower, upper+1):
        valid_count += 1

print(valid_count)