
N,Q = [int(x) for x in input().split(" ")]

locks = [{}] *(N+1)
for q in range(Q):
    que = [int(x) for x in input().split(" ")]

    if que[0] == 1:
        c = False
        for i in locks:
            if bool(i):
                for k in i:
                    if que[1]%k:
                        print("ja")
                        c = True
                        break
        if not c: print("nej")
    elif que[0] == 2:
        if que[1] not in locks[que[2]]:
            locks[que[2]][que[1]] = 0
        locks[que[2]][que[1]] += 1
    else:   
        locks[que[2]][que[1]] -= 1
        if locks[que[2]][que[1]] == 0:
            del locks[que[2]][que[1]]








