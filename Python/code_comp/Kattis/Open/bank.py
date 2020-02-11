import heapq
# http://challenge.csc.kth.se/2013/solutions.pdf
N, T = [int(x) for x in input().split(" ")]

q = [[] for _ in range(T)]
for i in range(N):
    c = [int(x) for x in input().split(" ")]
    q[c[1]].append(c[0])

que = []
heapq.heapify(que)
res = 0
for t in reversed(q):
    if not t:
        continue
    for customer in t:
        heapq.heappush(que, -customer)

    res += -(heapq.heappop(que))


print(res)
