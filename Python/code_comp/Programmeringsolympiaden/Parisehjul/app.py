import sys
import time as t
import collections as c

class Team:
    def __init__(self, i, to_ride):
        self.i = i
        self.to_ride = to_ride

file = open("3.txt","r")
N, n_vagnar = [int(x) for x in file.readline().split(" ")]


t0 = t.time()
team_list = [int(x) for x in file.readline().split(" ")]
team_list = [Team(i,team_list[i]) for i in range(len(team_list))]

wheel = c.deque([0 for x in range(n_vagnar)],maxlen = n_vagnar)

check = True
time = -1
next_in_line = 0 
lowest = 1000000000
count0 = n_vagnar 

while check:
    time += 1
    wheel.rotate()

    if wheel[0] != 0:
        if wheel[0].to_ride != 0:
            wheel[0].to_ride -= 1

        else:
            if next_in_line == len(team_list):
                wheel[0] = 0            
                count0 += 1 
                if count0 == n_vagnar:
                    check = False
                    break
                
                lowest = min([x.to_ride for x in wheel if x != 0])
                if next_in_line == len(team_list) and lowest >= 1:
                    time += (lowest)*n_vagnar
                    wheel = c.deque([Team(x.i,x.to_ride-lowest) if x != 0 else 0 for x in wheel])
                    lowest = min([x.to_ride for x in wheel if x != 0])
                    buffer = 0 
            else:
                wheel[0] = team_list[next_in_line]
                wheel[0].to_ride -= 1 
                lowest = min([x.to_ride for x in wheel if x != 0])

                next_in_line +=  1
                if count0 == 0 and lowest >= 1:
                    time += (lowest)*n_vagnar
                    wheel = c.deque([Team(x.i,x.to_ride-lowest) for x in wheel])
                    lowest = min([x.to_ride for x in wheel if x != 0])
                    buffer = 0 
    else:
        if next_in_line != len(team_list):
            wheel[0] = team_list[next_in_line]
            wheel[0].to_ride -= 1 
            lowest = min([x.to_ride for x in wheel if x != 0])

            count0 -= 1
            next_in_line +=  1
            if (next_in_line == len(team_list) or count0 == 0) and lowest >= 1 :
                
                time += (lowest)*n_vagnar
                wheel = c.deque([Team(x.i,x.to_ride-lowest) if x!=0 else 0 for x in wheel])
                lowest = min([x.to_ride for x in wheel if x != 0])
                buffer = 0 
            


print(time)
print(t.time()-t0)