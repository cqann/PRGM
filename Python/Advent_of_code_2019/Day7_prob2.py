import itertools

def pm(inpt,m,i,offset):
    if m == "0":
        return inpt[inpt[i+offset]]
    elif m == "1":
        return inpt[i+offset]

og = [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]

def program(inpt, i, phase, phase_supplied, raw_input):

    input_required = False
    to_return = None

    while inpt[i] != 99:
        cur = str(inpt[i])
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
            if not phase_supplied:
                inpt[inpt[i+1]] = phase
                phase_supplied = True
            else:
                if input_required:
                    return [inpt,i,phase,phase_supplied,to_return,False]
                inpt[inpt[i+1]] = raw_input
                input_required = True
            i += 2 
        elif op_code == "04" or op_code == 4:
            p1 = cur[-3] if len(cur) >= 3 else "0"
            to_return = pm(inpt,p1,i,1)
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
        
    return [inpt,i,phase,phase_supplied,to_return,True]

record = 0

for combo in itertools.permutations([5,6,7,8,9]):
    res1 = [list(og),0,combo[0],False,0,False]
    res2 = [list(og),0,combo[1],False,0,False]
    res3 = [list(og),0,combo[2],False,0,False]
    res4 = [list(og),0,combo[3],False,0,False]
    res5 = [list(og),0,combo[4],False,0,False]

    while res5[5] == False:
        res1 = program(res1[0],res1[1],res1[2],res1[3],res5[4])
        res2 = program(res2[0],res2[1],res2[2],res2[3],res1[4])
        res3 = program(res3[0],res3[1],res3[2],res3[3],res2[4])
        res4 = program(res4[0],res4[1],res4[2],res4[3],res3[4])
        res5 = program(res5[0],res5[1],res5[2],res5[3],res4[4])
        cur = res5[4]

    if cur > record:
        record = cur

print(record)
    












