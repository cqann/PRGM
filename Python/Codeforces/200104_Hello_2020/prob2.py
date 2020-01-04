import bisect
n = int(input())

arrays = []
for i in range(n):
    cur = input().split(" ")
    arrays.append([int(x) for x in cur[1:]])

highest = []
lowest = []
result = 0

for array in arrays:
    cur = False
    last = 1000000
    curh = 0
    curl = 1000000
    for a in array:
        if a > last:
            cur = True
        last = a
        curh = max(a,curh)
        curl = min(a,curl)
    if cur:
        result += 2*n 
    else:
        bisect.insort(highest,curh)
        lowest.append(curl)

l = len(lowest)
tot = result + l**2

for i in range(l):
    p = l - bisect.bisect_right(highest,lowest[i])
    result +=  l - bisect.bisect_right(highest,lowest[i])

result -= (tot-n**2)
        

print(result)


