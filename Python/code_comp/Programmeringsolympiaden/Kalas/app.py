import sys
import time

n_kalas, k = [int(x) for x in sys.stdin.readline().split(" ")]
s_w_h = [int(x) for x in sys.stdin.readline().split(" ")]
w_s = []
hours = 0 
check = True

for i in range(n_kalas):
    cur_kalas = [int(x) for x in sys.stdin.readline().split(" ")]
    afford =  (cur_kalas[0]-i)*10
    for s in [x for x in cur_kalas[2:] if x not in w_s]:       
        w_s.append(s)
        hours += s_w_h[s-1]
        if hours > afford:
            check = False
            break

    if len(w_s) == k or not check:
        break
    

if check:
    print("Ja")
else:
    print("Nej")

