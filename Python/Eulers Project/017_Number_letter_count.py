
digit_dic = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7}

tot = 11
for i in range(1,1000):
    n_split = []
    si = str(i)
    l = len(si)
    for i in range(l):
        n_split.append(int(si[i])*10**(l-i-1))
    if l > 2:
        if n_split[1] == 0 and n_split[2]== 0:
            tot += digit_dic[int(str(n_split[0])[0])] + digit_dic[100] 
        else:
            tot += 3 + digit_dic[int(str(n_split[0])[0])] + digit_dic[100]
            if n_split[1] != 10:
                tot += digit_dic[int(n_split[1])]
                tot += digit_dic[int(n_split[2])]
            else:
                tot += digit_dic[int(n_split[1])+int(n_split[2])]
    elif l > 1:
        if n_split[0] != 10:
            tot += digit_dic[int(n_split[0])]
            tot += digit_dic[int(n_split[1])]
        else:
            tot += digit_dic[int(n_split[0])+int(n_split[1])]
    else:
        tot += digit_dic[int(n_split[0])]
print(tot)

