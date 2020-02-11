
#0,1,2,3,

N = 7
antal = [1,2] + [None]*(N-2)
for i in range(2,N):
    antal[i] = antal[i-1] + antal[i-2]

print(antal[-1])

