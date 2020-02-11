
T = int(input())

for t in range(T):

    n,x = [int(x) for x in input().split(" ")]
    s = input()
    netto = 0 
    pattern = []
    pmax = 0
    pmin = 0
    res = 0
    for i in s:
        if i == "1":
            netto -= 1
        else:
            netto += 1

        pattern.append(netto)

        if netto < pmin: pmin = netto
        elif netto > pmax: pmax = netto


    if netto == 0 and x >= pmin and x <= pmax:
        print(-1)
        continue
    elif netto == 0:
        print(0)
        continue
    
    if netto < 0:
        cnetto = x-pmin
    else:
        cnetto = x-pmax

    res = pattern.count(x-cnetto)
    r = (pmax-pmin)//netto 
    n_res = res * r 
    
    print("RESULT: ", res,n_res)
    
    







