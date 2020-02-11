
A = [1,3,10,1,3,2]
B = [3,100,1,10,5]

arr = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for a in range(1,len(A)):
    for b in range(1,len(B)):
        if  A[a] == B[b]:
            arr[a][b] = arr[a-1][b-1] + 1
        else:
            arr[a][b] = max(arr[a][b-1],arr[a-1][b])


for i in arr:
    print(i)




# 