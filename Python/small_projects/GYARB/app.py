import math

Lx = 0.114
Ly = 0.046
Lz = 0.175

arr = []

for m in range(3):
    m_sq = (m/Ly)**2
    for n in range(3):
        n_sq = (n/Lz)**2
        for l in range(3):

            if l==0 and m==0 and n==0:
                continue 
            
            l_sq = (l/Lx)**2

            f = (343/2)*math.sqrt(l_sq + m_sq + n_sq)
            arr.append(f)

arr.sort()
for i in arr:
    print(i/25)
