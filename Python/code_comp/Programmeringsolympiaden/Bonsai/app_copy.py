import sys

class Klump:
    def __init__(self, i, branch):
        self.i = i
        self.n_buds = branch[0]
        self.buds = branch[1:]

def grow(start):
    splits = 0
    r_d = {}
    for bud in start.buds:
        if nexs[(start.i,bud)]:
            nexs[(start.i,bud)] = False
            nexs[(bud,start.i)] = False
            ret_val = grow(ks[bud])
            if ret_val in r_d:
                r_d[ret_val] += 1
            else:
                r_d[ret_val] = 0
            splits += 1

    if len(r_d) > 0:
        max_key = max(k for k, v in r_d.items())
        to_comp = max_key + r_d[max_key]
        return max(splits,to_comp) + 1 
    else:
        return splits

sys.setrecursionlimit(1000000000)
N = int(sys.stdin.readline())
ks = []
for i in range(N):
    ks.append(Klump(i,[int(x) for x in sys.stdin.readline().split(" ")]))
nexs = {} 
for klump in ks:
    for bud in klump.buds:
        nexs[(klump.i,bud)] = True

record = len(ks)
for i in range(len(ks)):
    time = grow(ks[i]) - 1 
    nexs = {k:True for (k,v) in nexs.items()}
    if time < record:
        record = time 
print(record)

