from heapq import *

N = int(input())
# DEN HÄR HAR BLVIT KAOS, lär mig inte riktigt ngt plus tror man behöver containers från c++, då en ordered dic med iterators hade varit bra
keys = []
dic = {}
dic[0] = []
for i in range(N):
    c = [x for x in input().split()]

    if c[0] == "add":
        com, e, g = c
        e, g = int(e), int(g)
        if e not in dic:
            dic[e] = []
        heappush(dic[e], -g)
        heappush(keys, -e)

    else:
        com, x = c
        x = int(x)
        not_used = []
        g_tot = 0
        try:
            cur_key = heappop(keys)
        except IndexError:
            print(0)
            continue
        while cur_key > x:
            try:
                cur_key = heappop(keys)
            except IndexError:
                print(0)
                continue
            while dic[cur_key] == []:
                try:
                    cur_key = heappop(keys)
                except IndexError:
                    print(0)
                    continue

        while True:
            if cur_key > x:
                break
            x += cur_key
            g_tot -= heappop(dic[-cur_key])

            while cur_key > x:
                try:
                    cur_key = heappop(keys)
                except IndexError:
                    print(0)
                    continue
                while dic[cur_key] == []:
                    try:
                        cur_key = heappop(keys)
                    except IndexError:
                        print(0)
                        continue

        keys = not_used + keys
        heapify(keys)
        print(g_tot)
