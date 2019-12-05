import math
def is_pal(n):
    nlist = list(str(n))
    for i in range(math.ceil(len(nlist))):
        if nlist[i] != nlist[len(nlist)-1-i]:
            return False
    return True

term1 = 100
term2 = 100
record = [0,0,0]

for i in range(900):
    for j in range(900):
        cur = term1 * term2
        if is_pal(cur) and cur > record[0]:
            record = [cur,term1,term2]
        term2 += 1
    term2 = 100
    term1 += 1

print(record)