from heapq import *
n = int(input())

items = [int(x) for x in input().split()]

m = int(input())

adj = [[] for _ in range(n)]

for i in range(m):
    c = [int(x)-1 for x in input().split()]

    adj[c[0]].append((c[1],c[2]+1))
    adj[c[1]].append((c[0],c[2]+1))
dis = [float("inf") for _ in range(n)]
dis[0] = 0
n_items = [0 for _ in range(n)]
n_items[0] = items[0]
proc = [False]*n
pq = [(0,0)]

while pq:
    brap = heappop(pq)
    cur = brap[1]
    proc[cur] = True
    cd = dis[cur]
    for nb in adj[cur]:
        if proc[nb[0]]: continue
        
        if cd + nb[1] < dis[nb[0]]:
            dis[nb[0]]  = cd + nb[1]
            n_items[nb[0]] = n_items[cur] + items[nb[0]]
            heappush(pq,(dis[nb[0]],nb[0]))
            
        elif cd + nb[1] == dis[nb[0]]:
            if n_items[cur] + items[nb[0]] > n_items[nb[0]]:
                n_items[nb[0]] = n_items[cur] + items[nb[0]]
    
    if cur == n-1: break

if dis[-1] == float("inf"):
    print("impossible")
else:
    print(dis[-1],n_items[-1])
        

        






