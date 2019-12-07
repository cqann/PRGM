n2 = 1 
n1 = 1 
cur = 0
index = 2
while len(str(cur)) < 1000:
    index += 1
    cur = n1 + n2
    n2 = n1
    n1 = cur

print(index)