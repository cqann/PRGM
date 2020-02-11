
N,Q = [int(x) for x in input().split(" ")]

locks = [0] *(N+1)
b_arr = [None] * (N+1)
for q in range(Q):
    que = [int(x) for x in input().split(" ")]

    if que[0] == 1:
        if locks[que[1]] == 0:
            print("nej")
        else:
            print("ja")
    elif que[0] == 2:
        if que[1] >= que[2]: continue  
        if b_arr[que[2]] == None:
            change = [que[2]*x for x in range(0,(N)//que[2]+1)]
            b_arr[que[2]] = change #Kan skapa fel här
        cb = b_arr[que[2]]
        if ((N)//que[2]) * que[2] + que[1] > N:
                cb = cb[:-1]
        for i in cb:
            locks[i+que[1]] += 1
    else:
        if que[1] >= que[2]: continue
        cb = b_arr[que[2]]
        if ((N)//que[2]) * que[2] + que[1] > N:
                cb = cb[:-1]
        for i in cb:
            locks[i+que[1]] -= 1







