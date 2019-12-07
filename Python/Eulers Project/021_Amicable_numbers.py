'''
READABLE VERSION
def d(n):
    divisors = [x for x in range(1,n//2+1) if n%x == 0]
    return sum(divisors)

am_num = []
for i in range(1,10000):
    d_of_i = d(i)
    if d(d_of_i) == i and i != d_of_i:
        am_num.append(i)

print(sum(am_num))
'''


def d(n):
    return sum([x for x in range(1,n//2+1) if n%x == 0])
print(sum([i for i in range(1,10000) if sum([k for k in range(1,sum([x for x in range(1,i//2+1) if i%x == 0])//2+1) if sum([x for x in range(1,i//2+1) if i%x == 0])%k == 0])==i and i != sum([x for x in range(1,i//2+1) if i%x == 0])]))