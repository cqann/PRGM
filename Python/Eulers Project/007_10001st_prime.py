def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


prime_list = []
to_try = 1

while len(prime_list)< 100000:
    if is_prime(to_try):
        prime_list.append(to_try)
    to_try += 1

print(prime_list)