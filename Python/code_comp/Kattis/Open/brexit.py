
c, p, x, l = [int(x) for x in input().split()]
x -= 1
l -= 1

# Skapa grafnät, ploppa bort L, rör dig till grannar, plobba bort granne om hälften av grannar borta

adj = [[] for _ in range(c)]
sizes = [0] * c
for i in range(p):
    trade = [int(x)-1 for x in input().split()]
    adj[trade[0]].append(trade[1])
    adj[trade[1]].append(trade[0])
    sizes[trade[0]] += 1
    sizes[trade[1]] += 1

org_size = list(sizes)

sizes[l] = 0

cur_layer = [l]
banned = {l}
while cur_layer:
    next_layer = []
    for country in cur_layer:
        for i in adj[country]:
            if i in banned:
                continue

            sizes[i] -= 1
            if sizes[i] < 1 + org_size[i]//2:
                next_layer.append(i)
                banned.add(i)

    cur_layer = next_layer

if sizes[x] < 1 + org_size[x]//2:
    print("leave")
else:
    print("stay")
