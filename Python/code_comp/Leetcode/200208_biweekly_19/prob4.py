

arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]

c_dic = {}

s = []
for i in range(len(arr)):
    s.append(i)

tp = {x: float("inf") for x in arr}

for i in range(1, len(arr)-1):
    s[i] = min(s[i-1]+1, s[i+1]+1, tp[arr[i]]+1)
    tp[arr[i]] = s[i] if s[i] < tp[arr[i]] else tp[arr[i]]

s[len(arr)-1] = min(s[i-1]+1, tp[arr[i]]+1)

print(s)
