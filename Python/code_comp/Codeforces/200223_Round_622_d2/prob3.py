n = int(input())
limits = [int(x) for x in input().split()]

delta_sum = 0
last = 0
for i in limits[1:]:
    delta_sum += i - last
    last = i

res = [None] * n 

if delta_sum >= 0:
    cur_big = 0
    for i in range(n):
        res[i] = limits[i] if limits[i] <= cur_big else<
