
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    z_c = arr.count(0)
    if sum(arr) + z_c == 0:
        print(z_c + 1)
    else:
        print(z_c)
