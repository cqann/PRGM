

N, M = [int(x) for x in input().split(" ")]

mapp = [[int(x) for x in input()] for _ in range(N)]

mapp.insert(0, [0 for _ in range(M)])
mapp.insert(0, [-2 for _ in range(M+4)])
mapp.append([0 for _ in range(M)])
mapp.append([-2 for _ in range(M+4)])
for i in range(1, N+3):
    mapp[i].insert(0, 0)
    mapp[i].insert(0, -2)
    mapp[i].append(0)
    mapp[i].append(-2)

count = 0


cur_layer = [(1, 1)]

while cur_layer != []:
    next_layer = []

    for cell in cur_layer:
        for neigh in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_x = cell[0] + neigh[1]
            new_y = cell[1] + neigh[0]
            cur_c = 0
            if mapp[new_y][new_x] == 0:
                next_layer.append((new_x, new_y))
                mapp[new_y][new_x] = -1
            elif mapp[new_y][new_x] == 1:
                count += 1

    cur_layer = next_layer

print(count)
