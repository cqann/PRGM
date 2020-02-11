import math
def p(cities, pop, b):
    count = 0
    for city in cities:
        req = math.ceil(city/pop) 
        count += req
        if count > b: 
            return False
    
    return True




for i in range(3):
    N, B = [int(x) for x in input().split(" ")]
    if N == -1 and B == -1: break

    cs = []
    cs_sum = 0
    for i in range(N):
        cur = int(input())
        cs.append(cur)
        cs_sum += cur

    lo = 1
    hi = cs_sum
    
    while lo + 1 != hi:
        mid = lo + (hi-lo)//2
        if p(cs,mid,B): 
            hi = mid 
        else:
            lo = mid
    
    print(hi)

    white = input()



