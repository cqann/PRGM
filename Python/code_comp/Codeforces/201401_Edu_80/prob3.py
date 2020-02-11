import math

def calc(n,m):
    if n == 1:
        return 1
    
    if m == 1:
        return (n*(n+1))/2

    return ((n*(n+1))/2 ) + calc(n,m-1)


def dimension_triangle(x, d):
    resss = 0
    if d == -1:
        return 1
    if d == 0:
        return x
    for i in range(x+1):
        resss += dimension_triangle(i, d-1)
    return resss

n,m = [int(x) for x in  input().split(" ")]

initial = 2 * n**m

print(dimension_triangle(n,m))





