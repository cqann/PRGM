
# Goldbach Conjecture, every even integer after can be written as the sum of two primes
import math


def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def goldbach(x):
    primes = [k for k in range(x+1) if is_prime(k) if k>1]
    possible_sums = []
    for primee in primes:
        for primet in primes:
            if primee + primet == x and not (str(primet)+" + "+str(primee)) in possible_sums:
                possible_sums.append(str(primee)+" + "+str(primet))


    for sum in possible_sums:
        print(sum)

def goldbach_count(x,only_int = False):
    primes = [k for k in range(x + 1) if is_prime(k) if k > 1]
    amount_sums = 0
    for primee in primes:
        for primet in primes:
            if primee + primet == x:
                amount_sums +=1

    amount_sums /= 2
    if only_int:
        return int(amount_sums)
    return str(x)+": " + str(int(amount_sums))

weird = []
 for i in range(1, 10001):
    if i%2==0:
        print(goldbach_count(i))
        if goldbach_count(i,only_int=True) < 5 and i>158:
            weird.append(i)

print(weird)