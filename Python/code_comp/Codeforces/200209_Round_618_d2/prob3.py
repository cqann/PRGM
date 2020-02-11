from collections import deque
n = int(input())


def f(x, y):
    return (x | y) - y


arr = [int(x) for x in input().split(" ")]

arr.sort()
d = deque(arr)

d.rotate()
arr = list(d)

print(" ".join([str(x) for x in arr]))
