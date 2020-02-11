import sys
import time

n_kalas, k = [int(x) for x in sys.stdin.readline().split(" ")]
s_w_h = [int(x) for x in sys.stdin.readline().split(" ")]
w_s = [0]*k
afford = 0
las = -1 
hours = 0 
check = True

for i in range(n_kalas):
    cur_kalas = [int(x) for x in sys.stdin.readline().split(" ")]
    hours += sum( [x-y for x,y in zip( [ s_w_h[i-1] for i in cur_kalas[2:] ], [ w_s[i-1] for i in cur_kalas[2:] ] ) ] )
    for i in [x for  x in cur_kalas[2:] if w_s[x-1] == 0]:
        w_s[i-1] = s_w_h[i-1]

    afford +=  (cur_kalas[0]-las-1)*10
    las = cur_kalas[0]

    if hours > afford:
        check = False 
        break



if check:
    print("Ja")
else:
    print("Nej")

