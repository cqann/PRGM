txt = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

rows = [[int(x) for x in row.split(" ")] for row in txt.split("\n")]
record = 0
def next_num(level,index,carry):
    global record
    if level >= 15:
        if record < carry:
            record = carry
        return
    left_index = index   
    right_index = index + 1
    next_num(level+1, left_index, carry + rows[level][index])
    next_num(level+1, right_index, carry + rows[level][index])

#next_num(0,0,0)
for i in range(15):
    print("new")
    ind = i if i!=14 else 13
    cur = rows[14][i] +75
    for l in range(13,0,-1):
        if ind == 0:
            print(l,ind)
            cur += rows[l][ind]
        elif ind == l:
            ind -= 1
            print(l,ind)
            cur += rows[l][ind]
        else:
            print(l,ind,ind-1)
            if rows[l][ind] < rows[l][ind-1]:
                ind -= 1
            cur += rows[l][ind]
    record = cur if cur > record else record


print(record)
#1074

