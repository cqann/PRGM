def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

i = 3

primes = []
composites = [1]
last_square = 1

while True:
    square = i * i
    diff = square - last_square
    diff_div = diff // 4
    ground = last_square
    for j in range(1,5):
        current = ground +  j * diff_div
        if is_prime(current):
            primes.append(current)
        else:
            composites.append(current)

    if len(primes) / (len(primes) + len(composites)) < 0.1:
        print("---DONE---")
        print(int(square**0.5))
        break

    last_square = square
    i += 2

    
    



