from heapq import *

while True:
    n, m = [int(x) for x in input().split()] 
    if [n,m] == [0,0]: break

    nodes = [[] for x in range(n)]
    for i in range(m):
        x, y, f = [float(d) for d in input().split(" ")] 
        x = int(x)
        y = int(y)
        f = 1/f
        nodes[x].append((y, f))
        nodes[y].append((x, f))

    visisted = [False] * n
    min_distance = [float("inf")] * n
    min_distance[0] = 1
    queue = []
    heappush(queue, (1,0))
    while queue:
        own_dis, node_index = heappop(queue)
        if visisted[node_index]: continue
        visisted[node_index] = True

        for adjecent in nodes[node_index]:
            adjecent_node, distance = adjecent
            if min_distance[adjecent_node] > own_dis * distance:
                min_distance[adjecent_node] = own_dis * distance
                heappush(queue, (own_dis * distance, adjecent_node))

    answer = 1/min_distance[n-1] 

    print(format(answer, ".4f"))

    