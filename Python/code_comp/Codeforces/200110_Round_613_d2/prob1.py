
n = int(input())

cmds = input()
counts = {"L":0,"R":0}

for c in cmds: counts[c]+=1

print(counts["L"] + counts["R"] + 1)

