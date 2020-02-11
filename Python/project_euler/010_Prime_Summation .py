def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

cur = 2
result = 0
while cur < 2000000:
    
    if is_prime(cur):
        result += cur
    cur += 1 

print(result)