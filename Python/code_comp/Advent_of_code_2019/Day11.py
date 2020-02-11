
def pm(prgm,m,i,offset):
    if m == "0":
        return prgm[i+offset]
    elif m == "1":
        return i+offset
    elif m == "2":
        return prgm[i+offset] + rel
    
prgm = [3,8,1005,8,328,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,28,1006,0,13,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,54,1,1103,9,10,1006,0,97,2,1003,0,10,1,105,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,91,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,113,2,109,5,10,1006,0,96,1,2,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,146,2,103,2,10,1006,0,69,2,9,8,10,1006,0,25,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,182,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,203,2,5,9,10,1006,0,0,2,6,2,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,236,2,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,263,2,105,9,10,1,103,15,10,1,4,4,10,2,109,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,301,1006,0,63,2,105,6,10,101,1,9,9,1007,9,1018,10,1005,10,15,99,109,650,104,0,104,1,21102,387508441116,1,1,21102,1,345,0,1106,0,449,21102,1,387353256852,1,21102,1,356,0,1105,1,449,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,179410308315,0,1,21102,1,403,0,1106,0,449,21101,206199495827,0,1,21102,414,1,0,1105,1,449,3,10,104,0,104,0,3,10,104,0,104,0,21102,718086758760,1,1,21102,1,437,0,1105,1,449,21101,838429573908,0,1,21102,448,1,0,1106,0,449,99,109,2,21202,-1,1,1,21102,1,40,2,21102,480,1,3,21101,470,0,0,1105,1,513,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,475,476,491,4,0,1001,475,1,475,108,4,475,10,1006,10,507,1102,0,1,475,109,-2,2106,0,0,0,109,4,2101,0,-1,512,1207,-3,0,10,1006,10,530,21101,0,0,-3,21202,-3,1,1,21201,-2,0,2,21102,1,1,3,21102,549,1,0,1105,1,554,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,577,2207,-4,-2,10,1006,10,577,22102,1,-4,-4,1106,0,645,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,596,0,0,1106,0,554,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,615,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,637,21201,-1,0,1,21101,637,0,0,106,0,512,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]
prgm += [0]*999999
rel = 0
i = 0

output_col = None
flip_output = True
facing = 0
x = 0 
y = 0
coord_dic = {(0,0):1}

while prgm[i] != 99:
    if (x,y) not in coord_dic:
        coord_dic[(x,y)] = 0

    cur = str(prgm[i])
    op_code = cur[-2:] if len(cur) >= 2 else prgm[i]
    if op_code == "01" or op_code == 1:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        p3 = cur[-5] if len(cur) >= 5 else "0"
        prgm[pm(prgm,p3,i,3 )] = prgm[pm(prgm,p1,i,1 )] + prgm[pm(prgm,p2,i,2 )]
        i += 4

    elif op_code == "02" or op_code == 2:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        p3 = cur[-5] if len(cur) >= 5 else "0"
        prgm[pm(prgm,p3,i,3 )] = prgm[pm(prgm,p1,i,1 )] * prgm[pm(prgm,p2,i,2 )]
        i += 4

    elif op_code == "03" or op_code == 3:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        prgm[pm(prgm,p1,i,1 )] = coord_dic[(x,y)]
        i += 2 

    elif op_code == "04" or op_code == 4:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        if flip_output:
            coord_dic[x,y] = prgm[pm(prgm,p1,i,1 )]
            flip_output = False
        else:
            direction = prgm[pm(prgm,p1,i,1 )]
            if direction == 0:
                facing = facing + 1 if facing != 3 else 0
                if facing%2 == 0:
                    y -= facing - 1
                else:
                    x -= facing - 2
            else:
                facing = facing - 1 if facing != 0 else 3
                if facing%2 == 0:
                    y -= facing - 1
                else:
                    x -= facing - 2
            flip_output = True

        i += 2

    elif op_code == "05" or op_code == 5:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if prgm[pm(prgm,p1,i,1 )] != 0:
            i = prgm[pm(prgm,p2,i,2 )]
        else:
            i += 3
        
    elif op_code == "06" or op_code == 6:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if prgm[pm(prgm,p1,i,1 )] == 0:
            i = prgm[pm(prgm,p2,i,2 )]
        else:
            i += 3

    elif op_code == "07" or op_code == 7:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        p3 = cur[-5] if len(cur) >= 5 else "0"
        if prgm[pm(prgm,p1,i,1 )] < prgm[pm(prgm,p2,i,2 )]:
            prgm[pm(prgm,p3,i,3 )] = 1
        else:
            prgm[pm(prgm,p3,i,3 )] = 0
        i += 4

    elif op_code == "08" or op_code == 8:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        p3 = cur[-5] if len(cur) >= 5 else "0"
        if prgm[pm(prgm,p1,i,1 )] == prgm[pm(prgm,p2,i,2 )]:
            prgm[pm(prgm,p3,i,3 )] = 1
        else:
            prgm[pm(prgm,p3,i,3 )] = 0
        i += 4   

    elif op_code == "09" or op_code == 9:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        rel += prgm[pm(prgm,p1,i,1 )]
        i += 2
    
screen = []

for k in coord_dic:
    try:
        screen[abs(k[1])][abs(k[0])] = "_" if coord_dic[k] == 0 else "#"
    except IndexError:
        for i in range(abs(k[1])-len(screen) +1):
            screen.append([])
        screen[abs(k[1])] += ["_"]*(1 + abs(k[0])-len( screen[abs(k[1])] ) )
        screen[abs(k[1])][abs(k[0])] = "_" if coord_dic[k] == 0 else "#"

for line in screen:
    print("".join(line))



