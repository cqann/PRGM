def find_max(dis, spt_check):
    result = 0
    result_index = None
    
    for i in range(len(dis)):
        if not spt_check[i] and dis[i] > result:
            result = dis[i]
            result_index = i

    return result, result_index

while True:
    n, m = [int(x) for x in input().split()] 
    if [n,m] == [0,0]: break

    nodes = [[] for x in range(n)]
    for i in range(m):
        x, y, f = [float(d) for d in input().split(" ")] 
        x = int(x)
        y = int(y)
        nodes[x].append((y, f))
        nodes[y].append((x, f))

    spt_check = [False] * n
    dis = [0] * n
    dis[0] = 1
    while True:
        own_dis, node_index = find_max(dis, spt_check)
        if node_index == None: break
        spt_check[node_index] = True
        for adjecent in nodes[node_index]:
            adjecent_node, distance = adjecent
            if not spt_check[adjecent_node] and dis[adjecent_node] < own_dis * distance:
                dis[adjecent_node] = own_dis * distance
                
    answer = dis[n-1]   
    print(format(answer, ".4f"))

    