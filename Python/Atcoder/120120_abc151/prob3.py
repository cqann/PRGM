

N, M = [int(x) for x in input().split(" ")]

subms = [input().split(" ") for i in range(M)]

setto = {k:False for k in range(1,N+1)}
penalties = 0 
correct = 0 
for sub in subms:
    sub[0] = int(sub[0])
    if setto[sub[0]] == False:
        if sub[1] == "WA":
            penalties += 1
        else:
            correct += 1
            setto[sub[0]] = True

print(correct, penalties)








