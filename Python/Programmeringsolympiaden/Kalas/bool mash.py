import sys
import time

n_kalas, k = [int(x) for x in sys.stdin.readline().split(" ")]
s_w_h = [int(x) for x in sys.stdin.readline().split(" ")]
w_s = [0]
afford = 0
las = -1 
hours = 0 
list_w_hours = []
list_w_time = []

for i in range(n_kalas):
    cur_kalas = [int(x) for x in sys.stdin.readline().split(" ")]
    m_n_w = [x for x in cur_kalas[2:] if x not in w_s]
    hours += sum([s_w_h[x-1] for x in m_n_w])
    w_s += m_n_w
    list_w_hours.append(hours)      

    afford +=  (cur_kalas[0]-las-1)*10
    list_w_time.append(afford)
    las = cur_kalas[0]


if all([x >= y for x,y in zip(list_w_time, list_w_hours)]):
    print("Ja")
else:
    print("Nej")

