def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return int((a*b)/gcd(a,b))

factors = {1:[1]}
def factors_of(n):
    if n in factors:
        return factors[n]
    ret = [n]
    for i in range(n,0,-1):
        if n%(n/i) == 0:
            factors[n] = factors_of(i) + ret
    return factors[n]
n = int(input())

prime_found = False
big1 = 0
big2 = 0
print(factors_of(56))
for a in input().split(" "):
    if a > big1:
        if prime_found:
            if is_prime(a):
                big2 = big1
                big1 = a
        else:
            big2 = big1
            big1 = a
            if is_prime(big2):
                prime_found = True


