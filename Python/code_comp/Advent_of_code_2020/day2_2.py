


inputs = [x[:-1] for x in open("day2.txt","r")]
valid_count = 0
for entry in inputs:     
    rule, password = entry.split(":")
    limit, letter = rule.split(" ")
    password = password[1:]
    index1, index2 = [int(x)-1 for x in limit.split("-")]

    a = password[index1] == letter
    b = password[index2] == letter
    
    if a != b :
        valid_count += 1

print(valid_count)