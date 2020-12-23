regex = set()
hard = set()

with open("019/valids.txt", "r") as file:
    erik = True
    for line in file:
        if line == "\n":
            erik = False
            continue
        if erik: 
            regex.add(line.strip())
        else: 
            hard.add(line.strip())

print((regex.symmetric_difference(hard)))