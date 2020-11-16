import time
t0 = time.time()
def is_prime(x):
    if x == 1: return False
    i = 2
    while i*i < x + 1:
        if x%i == 0:
            return False
        i += 1
    return True

n = 10**6
prime_or_not = [True] * n
sums = [0]

prime_or_not[0] = False
i = 2
while i*i < n + 1:
    j = 2
    while i * j < n:
        prime_or_not[i * j - 1] = False
        j += 1
    i += 1
    
for j in range(len(prime_or_not)):
    if prime_or_not[j-1]:
        sums.append(sums[-1] + j)
        
p1 = 0
record_len = 1
record = 0
while p1 + record_len < len(sums):
    cur_sum = sums[p1 + record_len] - sums[p1]
    if cur_sum < n:
        if prime_or_not[cur_sum-1]:
            record_len += 1
            record = cur_sum
            p1 = -1
    else:
        record_len += 1
        p1 = -1
    p1 += 1
    
print(record)
print(time.time() - t0)
