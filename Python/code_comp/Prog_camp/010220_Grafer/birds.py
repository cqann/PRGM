
N,M,K = [int(x) for x in input().split(" ")]

adj = [[] for _ in range(N)]
for i in range(N-1):
    cur = [int(x)-1 for x in input().split(" ")]
    adj[cur[0]].append(cur[1])
    adj[cur[1]].append(cur[0])

proc = [False for _ in range(N)]
order = []

def dfs(ind,subtree):
    proc[ind] = True
    for i in range(len(adj[ind])):
        nbr = adj[ind][i]
        if not proc[nbr]:
            dfs(nbr,subtree)
    
    order[subtree].append(ind+1)
    return

proc[K-1] = True
doable_i = -1
for i in range(len(adj[K-1])):
    nbr = adj[K-1][i]
    order.append([])
    dfs(nbr,i)
    if len(order[i]) > M - 1 :
        doable_i = i
        break
    
ans = -1 if doable_i == -1 else " ".join([str(x) for x in list(reversed(order[doable_i])) + [K] ])
print(ans)




