n = int(input())
limits = [int(x) for x in input().split()]

delta_sum = 0
last = 0
for i in limits[1:]:
    delta_sum += i - last
    last = i

print(delta_sum)
