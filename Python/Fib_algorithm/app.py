import math

def num_ways_fib(n):
    fib_list = [None]*(n+2)
    fib_list[0] = 0
    fib_list[1] = 1
    for i in range(n):
        if i == n:
            break
        fib_list[i+2] = fib_list[i]+fib_list[i+1]

    print(fib_list)

    return(fib_list[n+1])

def num_ways(n):
    new_n = n + 1
    res = 0
    for i in range(int((new_n/2).__floordiv__(1)+1)):
        seq_length = new_n - i
        twos = i
        ones = seq_length - i
        res += dimension_triangle(ones, twos-1)

    return(res)

def new_num_ways(n):
    res = 0
    for i in range(int(((n)/2).__floordiv__(1)+1)):
        res += dimension_triangle(n-2*i,i-1)
    return res


def dimension_triangle(x, d):
    resss = 0
    if d == -1:
        return 1
    if d == 0:
        return x
    for i in range(x+1):
        resss += dimension_triangle(i, d-1)
    return resss

num_ways_fib(50)
for i in range(1,50):
    print(new_num_ways(i))

# F_n = \sum_{i=0}^{\lfloor n/2\rfloor}f(n-2i,i-1)
# f(x,y) = \begin{cases}1 & if\space y = -1\\x & if\space y = 0\\\sum_{k=0}^x f(k,y-1) & if\space y>1\space and\space y\in N \end{cases}
