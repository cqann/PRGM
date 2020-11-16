import time


t0 = time.time()
triangle = [[1]]
count = 0
for i in range(100):
    triangle.append([])
    last = 0
    for x in triangle[-2]:
        val = x + last
        if val > 10**6: count += 1
        triangle[-1].append(val)
        last = x
    triangle[-1].append(1)

print(count)
print(time.time()-t0)