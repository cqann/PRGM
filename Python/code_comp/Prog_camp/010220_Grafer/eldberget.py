
R,C,K = [int(x) for x in input().split(" ")]

mapp = [[x for x in input()] for _ in range(R)]

mapp.insert(0,['#' for _ in range(C)])
mapp.append(['#' for _ in range(C)])
for i in range(R+2):
    mapp[i].insert(0,'#')
    mapp[i].append('#')
mapp[1][1] = 0
neighbours = [(-1,0),(1,0),(0,1),(0,1)]

cur_layer = [(1,1)]



while cur_layer != []:
    next_layer = []
    
    for cell in cur_layer:
        for neigh in neighbours:
            new_x = cell[0] + neigh[1]
            new_y = cell[1] + neigh[0]
            if mapp[new_y][new_x] == '.':
                next_layer.append((new_x,new_y))
                mapp[new_y][new_x] = mapp[cell[1]][cell[0]] + 1
            
    cur_layer = next_layer

'''
for i in mapp:
    s = ""
    for j in i:
        s += str(j)
    print(s)
'''
answer = mapp[-2][-2] if mapp[-2][-2] != '.' else "nej"

print(answer)