import math
def count_divs(n):
    count = 0
    sqn = math.sqrt(n)
    for i in range(1,math.floor(sqn)):
        if n%i == 0:
            count += 1

    to_return = count*2
    if int(sqn) == sqn:
        to_return += 1 
    return to_return

def make_tri(n):
    return int((n*(n+1))/2)

print(count_divs(28))
n_divisors = 0
cur = 0
j = 1
while n_divisors < 500:
    cur += j
    cur_divs =  count_divs(cur)
    if cur_divs > n_divisors:
        n_divisors = cur_divs
        print(cur_divs)
    
    j+=1 

print(cur)
