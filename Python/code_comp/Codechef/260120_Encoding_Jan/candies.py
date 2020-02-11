import math
t =int(input())
for i in range(t):

    N, M, K = [int(x) for x in input().split(" ")]

    c_sum = N + M

    s = math.ceil(K / (c_sum*1.0))
    other = K - M*(s-1) 
    if N*s > other:
        print(other)
    else:
        print(N*s)