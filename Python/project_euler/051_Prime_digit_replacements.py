import time
from math import log
from itertools import permutations as perms
t0 = time.time()
#DE E KAOS
primes = set()
def is_prime(x):
    global primes 
    if x in primes: return True
    if x == 1: return False
    i = 2
    while i*i < x + 1:
        if x%i == 0:
            return False
        i += 1

    primes.add(x)
    return True


l = 4
done = False
while not done:
    for i in range(1,l):
        to_vary = set(perms([1]*i + [0]*(l-i)))
        n_normal = l - i 
        for j in range(10**n_normal + 1, 10**(n_normal + 1), 2):
            actual_j = (str(j)[0:-1])
            for p in to_vary:
                found = True
                count = 0
                result = []
                limit = 2
                for k in range(10):
                    cur = ""
                    j_index = 0
                    first = True
                    skip_0 = False
                    for b in p:
                        if first and b == 1 and k==0:
                            skip_0 = True
                            break
                        first = False
                        if b == 0:
                            cur += actual_j[j_index]
                            j_index += 1
                        else:
                            cur += str(k)
                    if skip_0: 
                        limit -= 1
                        continue
                    cur += str(j)[-1]
                    cur = int(cur)
                    if not is_prime(cur):
                        count += 1
                        if count > limit:
                            found = False
                            break
                    else:
                        result.append(cur)

                if found:
                    print(p, result)
                    done = True
                    break
            if done: break
        if done: break
    l += 1


print(time.time() - t0)
