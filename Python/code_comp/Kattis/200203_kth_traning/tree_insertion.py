from math import factorial as fc


def place_val(ind, vali):
    adj[ind][0] += 1
    if arr[vali] < arr[ind]:
        if adj[ind][1] == None:
            adj[ind][1] = vali
        else:
            place_val(adj[ind][1], vali)
    else:
        if adj[ind][2] == None:
            adj[ind][2] = vali
        else:
            place_val(adj[ind][2], vali)
    return


def n_choose_k(n, k):
    return fc(n) // (fc(k) * fc(n - k))


def ways(a):
    if len(a) <= 1:
        return 1
    else:
        s = []
        g = []
        for i in range(1, len(a)):
            if a[i] < a[0]:
                s.append(a[i])
            else:
                g.append(a[i])
        return n_choose_k(len(a)-1, len(s)) * ways(s) * ways(g)


while True:
    N = int(input())
    if N == 0:
        break
    arr = [int(x) for x in input().split(" ")]
    '''
    adj = [[0, None, None] for _ in range(N)]
    adj[0] = [0, None, None]
    for i in range(1, N):
        place_val(0, i)

    res = 1

    for a in adj:
        left = a[1]
        right = a[2]
        tot = a[0]
        if tot == 0:
            continue
        if left == None and right != None:
            left = right
        res *= n_choose_k(tot, adj[left][0]+1)
    '''
    print(ways(arr))
