import sys

N,l,v = [int(x) for x in sys.stdin.readline().split(" ")]
treads = []

for i in range(N):
    cur = [int(x) for x in sys.stdin.readline().split(" ")] 
    cur.append(cur[2]/(cur[1]-cur[0]))
    treads.append(cur)

record = l*v

def go(x,time,new_list):
    global record
    if len(new_list) == 0:
        time += v*(l-x)
        if time < record:
            record = time
        return

    lowest = min([p[1] for p in new_list])
    first_layer = [p for p in new_list if p[0]<= lowest]
    
    for tread in first_layer:
            if tread[3] < v:
                go(tread[1],time + (tread[0]-x)*v + tread[2],[p for p in new_list if p[0] >= tread[1]])
        

go(0,0,treads)
    

print(record)
