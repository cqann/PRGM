

K = int(input())

s1,l1 = [x for x in input().split(" ")]
s2,l2 = [x for x in input().split(" ")]
l1 = int(l1)
l2 = int(l2)
if len(s1) > len(s2):
    s2,l2,s1,l1 = s1,l1,s2,l2

res = ""


def add_l(f1,f2,ind,string):
    global res
    print(f1,f2)
    if len(string) <= ind:
        return 
    if len(f1) < l1 : f1 += string[ind]
    if len(f2) < l2 : f2 += string[ind]

    if len(f1) == l1 and len(f2) >= len(f1):
        for i in range(1,len(s1)+1):
            if s1[-i] == f2[-i]:
                print(12341293812839938)
                if s2[-i:] == f2[-i:]:
                    res += f2 + "<"*(i+1)
                    return 
                break
            

    add_l(f1,f2,ind+1,s1)
    add_l(f1,f2,ind+1,s2)
    return
    
    

    
#add_l("","",0,s2)
t = ""
for i in s2:
    t += i
    if len(t) >= l1:
        to_add = ""
        for j in range(1,len(s1)+1):
            if s1[-j:] == t[-j:]:
                to_add = t + "<"*(j)
                
        res += to_add
                

c = 0
for i in list(reversed(res)):
    if i != "<":
        break
    c+=1
res += s2[-c:]
print(res)







