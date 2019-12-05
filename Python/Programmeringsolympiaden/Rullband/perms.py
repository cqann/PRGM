import itertools
import sys

N,l,v = [int(x) for x in sys.stdin.readline().split(" ")]
treads = []
for i in range(N):
    treads.append([int(x) for x in sys.stdin.readline().split(" ")])

combos = []
record = l*v
for r in range(1,N+1):
    for i in itertools.permutations(range(N),r):
        combo = list(i)
        print(combo)
        x = 0
        dis = 0
        time = 0
        for i in combo:
            tread = treads[i]
            to_walk = abs(tread[0]-x)
            dis += to_walk
            time += to_walk * v
            x = tread[1]
            time += tread[2]

        time += (l-x)*v
        if time < record:
            record = time 
            best = combo
    

print(record)
