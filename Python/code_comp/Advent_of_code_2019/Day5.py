def pm(inpt,m,i,offset):
    if m == "0":
        return inpt[inpt[i+offset]]
    elif m == "1":
        return inpt[i+offset]

inpt = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

i = 0

while inpt[i] != 99:
    print("\n".join([str(i) for i in inpt]))
    cur = str(inpt[i])
    if(cur == "1006"):
        print("")

    op_code = cur[-2:] if len(cur) >= 2 else inpt[i]
    if op_code == "01" or op_code == 1:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        p3 = cur[-5] if len(cur) >= 5 else "0"
        inpt[inpt[i+3]] = pm(inpt,p1,i,1) + pm(inpt,p2,i,2)
        i += 4
    elif op_code == "02" or op_code == 2:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        inpt[inpt[i+3]] = pm(inpt,p1,i,1) * pm(inpt,p2,i,2)
        i += 4
    elif op_code == "03" or op_code == 3:
        inpt[inpt[i+1]] = int(input("Input required: "))
        i += 2
    elif op_code == "04" or op_code == 4:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        print("Output: " + str(pm(inpt,p1,i,1)))
        i += 2
    elif op_code == "05" or op_code == 5:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if pm(inpt,p1,i,1) != 0:
            i = pm(inpt,p2,i,2)
        else:
            i += 3
    elif op_code == "06" or op_code == 6:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if pm(inpt,p1,i,1) == 0:
            i = pm(inpt,p2,i,2)
        else:
            i += 3
    elif op_code == "07" or op_code == 7:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if pm(inpt,p1,i,1) < pm(inpt,p2,i,2):
            inpt[inpt[i+3]] = 1
        else:
            inpt[inpt[i+3]] = 0
        i += 4
    elif op_code == "08" or op_code == 8:
        p1 = cur[-3] if len(cur) >= 3 else "0"
        p2 = cur[-4] if len(cur) >= 4 else "0"
        if pm(inpt,p1,i,1) == pm(inpt,p2,i,2):
            inpt[inpt[i+3]] = 1
        else:
            inpt[inpt[i+3]] = 0
        i += 4
    else:
        print(f"Error: intcode '{op_code}' not supported.")
        break








