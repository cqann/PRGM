import math
def is_prime(num):
    for i in range(2,math.ceil(math.sqrt(num))+1):
        if(num/i == num//i and num != i):
            return False

    return True

def is_in(n,l):
    for i in range(len(l)):
        if n == l[i]:
            return True

    return False

n = 600851475143
list_of_primes = []
varying = n

sqrtn = int(math.sqrt(varying))+1
for i in range(2,sqrtn):
    if is_prime(i):
        if n/i == n//i:
            list_of_primes.append(i)


print(list_of_primes)