
l = [0,1,9,7,5,12,10,2,1]

def lis(x):
    L,P = [None]*len(x), [None]*len(x)
    for j in range(len(x)):
        less_idx = [i for i in range(j) if x[i] < x[j]]
        best = None
        max_len = 1
        for i in less_idx:
            if L[i] +1 > max_len:
                max_len = L[i] +1 
                best = i
        L[j] = max_len
        P[j] = best

    curr = L.index(max(L))
    res = []
    while curr != None:
        res.append(curr)
        curr = P[curr]
            
    return res

print(lis(l))


