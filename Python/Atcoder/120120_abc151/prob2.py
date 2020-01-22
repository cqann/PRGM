

N, K, M = [int(x) for x in input().split(" ")]

scores = [int(x) for x in input().split(" ")]

scores_sum = sum(scores)

vary = 0
while vary <= K:
    avg = (vary + scores_sum)/(N*1.0)
    if avg >= M:
        break
    vary += 1


if vary != K+1:
    print(vary)
else:
    print(-1)






