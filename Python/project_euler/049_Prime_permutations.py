def is_prime(x):
    i = 2
    while i*i < x + 1:
        if x%i == 0:
            return False
        i += 1
    return True

def perm(x, y):
    return sorted(str(x)) == sorted(str(y))

primes = set()
for i in range(1000,10000):
    if is_prime(i):
        primes.add(i)

start_val = 1000
offset = 1
while start_val <= 9998:
    if start_val not in primes:
        start_val += 1
        continue
    while start_val + 2 * offset < 10000:
        val1 = start_val
        val2 = val1 + offset
        val3 = val2 + offset
        if perm(val1,val2) and perm(val1, val3):
            if val2 in primes and val3 in primes:
                print(val1, val2, val3)
        offset += 1

    start_val += 1
    offset = 1