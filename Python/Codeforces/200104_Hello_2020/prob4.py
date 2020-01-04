import bisect

n = int(input())
lectures = [[int(x) for x in input().split(" ")] for i in range(n)]


a_tbans = set()
b_tbans = set()

ab = []

happy = True 

for lecture in lectures:
    acur = True
    bcur = True 
    a_to_add = []

    for i in ab:
        if max(lecture[0],i[0]) <= min(lecture[1],i[1]):
            if lecture[1] > i[1]:
                c_l = list(i)
                c_l[1] = lecture[1]
                a_to_add.append(c_l)
                c#JAG ORKAR INTE, hejdå
            if lecture[0] < i[0]:
                i[0] = lecture[0]
            acur = False 
        for 


    if not acur:
        ab.append((lecture[0],lecture[1]))
    
    for i in range(lecture[2],lecture[3]+1):
        if i in b_tbans:    
            bcur = False
            break
        b_tbans.add(i)
    
    if acur != bcur:
        happy = False
        break


if happy:
    print("YES")
else:
    print("NO")




