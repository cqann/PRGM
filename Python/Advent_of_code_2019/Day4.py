
def never_decrease(n):
    string_n = str(n)
    last = 1
    for i in string_n:
        if int(i) < last:
            return False
        last = int(i)
    return True

def contain_double(n):
    string_n = str(n)
    dic = {k:0 for k in range(0,10)}
    for i in string_n:
        dic[int(i)] = dic[int(i)] + 1 
    
    for key in dic:
        if dic[key] == 2:
            return True

    return False 

count = 0
for i in range(178416,676462):
    if contain_double(i) and never_decrease(i):
        count += 1 

print(count)