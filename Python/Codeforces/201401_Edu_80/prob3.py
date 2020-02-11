import math

def calc(n,m):
    if n == 1:
        return 1
    
    if m == 1:
        return (n*(n+1))/2

    return ((n*(n+1))/2 ) + calc(n,m-1)



n,m = [int(x) for x in  input().split(" ")]

initial = 2 * n**m
n_desc = n


print(calc(n,m))





