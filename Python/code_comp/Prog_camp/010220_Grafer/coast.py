

N,M = [int(x) for x in input().split(" ")]

mapp = [[int(x) for x in input()] for _ in range(N)]
mapp.insert(0,[0 for _ in range(M)])
mapp.append([0 for _ in range(M)])
for i in range(N+2):
    mapp[i].insert(0,0)
    mapp[i].append(0)



count = 0 

for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        if mapp[y][x] == 1: continue
        
        cur_c = 0
        for nbr in [(0,-1),(0,1),(-1,0),(1,0)]:
            ch_x = x + nbr[0]
            ch_y = y + nbr[1]
            if ch_x >= 0 and ch_x < M + 2 and ch_y >= 0 and ch_y < N + 2:
                if mapp[ch_y][ch_x] == 1:
                    cur_c += 1
        
        if cur_c != 4:
            count += cur_c

print(count)
            
