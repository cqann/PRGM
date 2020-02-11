import bisect
N, Q, H, W = [int(x) for x in input().split(" ")]


# create sorted list of rocks
rocks = []
for i in range(N):
    c = [int(x) for x in input().split(" ")]
    if c[1] < 82 or c[1] > 282:
        continue
    bisect.insort(rocks, (c[1], c[2], c[0]))

# incoming crash function


def find_crash(x, y):
    ind = bisect.bisect_left(rocks, (x, y, 0))
    crash_ind = -1
    weight = 0
    for i in range(ind, len(rocks)):
        if rocks[i][2] == 1:
            if rocks[i][1] > y:
                crash_ind = i
                weight = rocks[i][1] - y
                break
        else:
            if y > rocks[i][1]:
                crash_ind = i
                weight = y - rocks[i][1]
                break

    return crash_ind, weight


def find_backcrash(x, y):
    ind = bisect.bisect_left(rocks, (x, y, 0)) - 1
    crash_ind = -1
    weight = 0
    for i in range(ind, -1, -1):
        if rocks[i][2] == 1:
            if rocks[i][1] > y:
                crash_ind = i
                weight = rocks[i][1] - y
                break
        else:
            if y > rocks[i][1]:
                crash_ind = i
                weight = y - rocks[i][1]
                break

    return crash_ind, weight


# create node list
edges = [([], []) for _ in range(len(rocks))]  # [[forward][backwards]]
for i in range(len(rocks) - 1):
    ci, w = find_crash(rocks[i][0], rocks[i][1])
    if ci == -1:
        continue
    edges[i][0].append((ci, w))
    edges[ci][1].append((i, w))

# add weights
weights = [0]*len(rocks)
for i in range(len(rocks)-1, -1, -1):
    for child in edges[i][1]:
        weights[child[0]] = weights[i] + child[1]

arr = []
for q in range(Q):
    x1, y1, x2, y2 = [int(x) for x in input().split(" ")]
    if x2 < x1:
        x1, y1, x2, y2 = x2, y2, x1, y1
    i1, dy1 = find_crash(x1, y1)
    i2, dy2 = find_backcrash(x2, y2)

    dx = x2-x1
    qdy = abs(y1 - y2)
    if i2 == -1 or i1 == -1 or i2 < i1:
        arr.append(dx + qdy)
        continue

    while not edges[i2][1]:
        i2, dy2 = find_backcrash(rocks[i2][0]-1, y2)
        if i2 <= 0:
            i2, dy2 = find_backcrash(x2, y2)
            break

    dy = dy1 + dy2
    print(dy)
    print(rocks[i1], rocks[i2])
    dy += weights[i1] - weights[i2]
    dy = qdy if qdy > dy else dy
    ans = dy + dx
    print(dy, dx)
    arr.append(ans)

for a in arr:
    print(a)


'''
test that doesnt work
8 1 20 100
2 8 3
1 20 10
2 94 12
2 70 4
1 40 6
2 4 6
1 17 3
1 26 18
95 2 77 16

'''
