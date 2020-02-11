import bisect as bs
t = int(input())

for test in range(t):

    n = int(input())

    stds = [int(x) for x in input().split(" ")]

    stds.sort()

    diff = stds[n]-stds[n-1]

    print(diff)
