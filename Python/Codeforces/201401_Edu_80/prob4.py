def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())

for i in range(int(n**0.5),0,-1):
    if n % i == 0:
        
        if abs(n / gcd(i,int(n/i) ) - n) < 0.000001:
            a = i
            b = int(n/i)
            break

print(a, b)

