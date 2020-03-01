n, tot = [int(x) for x in input().split()]
dv = [[int(x) for x in input().split()] for _ in range(n)]
l1 = -(min([x[1] for x in dv]))
l2 = 1010000
while abs(l1-l2) > 0.0000001:
    mid = l1 + (l2-l1)/2.0
    if sum([(s[0])/(s[1]+mid) for s in dv]) < tot:
        l2 = mid
    else:
        l1 = mid
print(l1 + (l2-l1)/2.0)