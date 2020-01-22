from math import sqrt, ceil


T = int(input())

for t in range(T):

    n,d = [int(x) for x in input().split(" ")]

    if 2*sqrt(d)-1 <= n:
        print("YES")
    else:
        print("NO")
    








