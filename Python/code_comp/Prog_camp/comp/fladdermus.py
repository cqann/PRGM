import bisect
N, Q, H, W = [int(x) for x in input().split(" ")]

rocks = []
for i in range(N):
    c = [int(x) for x in input().split(" ")]
    bisect.insort(rocks, (c[1],c[2],c[0]))



for q in range(Q):
    x1,y1,x2,y2 = [int(x) for x in input().split(" ")]
    if x2 < x1:
        x1,y1,x2,y2 = x2,y2,x1,y1
    i1 = bisect.bisect_left(rocks,(x1,y1,0))
    i2 = bisect.bisect_left(rocks,(x2,y2,0))

    dx = x2-x1
    dy = 0
    cy = y1
    for i in range(i1,i2):
        cr = rocks[i]
        if cr[2] == 1:
            if cr[1] > cy:
                dy += cr[1]-cy
                cy = cr[1]
        else:
            if cr[1] < cy:
                dy += cy - cr[1]
                cy = cr[1]
    dy += abs(cy-y2)

    print(dy+dx)


