
'''
inpt = "10\n17 15 16 16 15 14 13 12 13 9"
inpt = inpt.split("\n")
N,obs = inpt[0],inpt[1]
obs = obs.split(" ")
count = -1
last = 0
for i in [int(x) for x in obs]:
    if i > last:
        count += 1
    last = i
print(count)
'''

import sys

for inpt in sys.stdin:

    if inpt not in [str(x)+"\n" for x in range(0,150 )]:
        inpt = inpt[0:len(inpt)-1]
        obs = inpt.split(" ")
        print(obs)
        count = -1
        last = 0
        for i in obs:
            if int(i) > int(last):
                count += 1
            last = i
        print(count)