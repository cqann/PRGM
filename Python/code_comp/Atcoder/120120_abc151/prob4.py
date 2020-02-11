

N, M = [int(x) for x in input().split(" ")]

subms = [input().split(" ") for i in range(M)]

setto = set()
penalties = 0 
correct = 0 
for sub in subms:
    if sub[0] not in setto:
        if sub[1] == "WA":
            penalties += 1
        if sub[1] == "AC":
            correct += 1
            setto.add(sub[0])

print(correct, penalties)








