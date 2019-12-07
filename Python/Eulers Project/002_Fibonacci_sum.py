second = 1 
last = 1
result = 0
cur = 0
while cur < 4000000:
    cur = last + second
    result += cur if cur%2==0 else 0
    second = last
    last = cur
print(result)
