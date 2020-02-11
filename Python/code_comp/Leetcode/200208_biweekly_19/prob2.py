
arr = [7, 7, 7, 7, 7, 7, 7]
k = 7
th = 7
c = 0
cs = sum(arr[0:k-1])

for i in range(k-1, len(arr)):
    cs += arr[i]
    if cs / (k*1.0) >= th:
        c += 1
    cs -= arr[i-k+1]

print(c)
