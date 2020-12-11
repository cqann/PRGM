

file = open("day1.txt","r")
entries = [int(x) for x in file]

for i, a in enumerate(entries):
    for j, b in enumerate(entries[i+1:]):
        if a + b == 2020:
            print(a,b,a*b)



