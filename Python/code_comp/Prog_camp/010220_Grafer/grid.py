from heapq import *


n,m = [int(x) for x in input().split(" ")]
grid = [[int(x) for x in input() ]for _ in range(n)]

adj = [[None]*m for _ in range(n)]
for y in range(len(grid)):
    for x in range(len(grid[y])):
        cur = []
        val = grid[y][x]

        if val == 0:
            continue
        for neigh in [(0,-val),(0,val),(-val,0),(val,0)]:
            nx = x + neigh[0]
            ny = y + neigh[1]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                cur.append((nx,ny))
        adj[y][x] = cur


dst = [[float('inf')]*m for _ in range(n)]
dst[0][0] = 0
proc = [[False]*m for _ in range(n)]
pq = [(0,(0,0))]

while pq:
    cur = heappop(pq)
    c_dst = cur[0]
    c_coord = cur[1]
    if adj[c_coord[1]][c_coord[0]] == None: 
        continue
    for nbr in adj[c_coord[1]][c_coord[0]] :
        if proc[nbr[1]][nbr[0]]:
            continue
        n_dst = c_dst + 1
        if n_dst < dst[nbr[1]][nbr[0]]:
            dst[nbr[1]][nbr[0]] = n_dst
            heappush(pq, (n_dst, (nbr[0],nbr[1])))
    proc[c_coord[1]][c_coord[0]] = True
    if c_coord[1] == n-1 and c_coord[0] == m-1: break
'''
for i in dst:
    print(i)
'''
ans = -1 if dst[-1][-1] == float("inf") else dst[-1][-1]
print(ans)