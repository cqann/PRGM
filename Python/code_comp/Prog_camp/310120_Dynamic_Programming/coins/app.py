#DYNAMISK PROGRAMMERING
result = 0
coins = [1,2,5,10,20,50,100,200]
d = {1:5,5:10,10:20,20:50,50:100,100:200,200:500,500:1000}


def gen_nums(carry, curCoin,N):
    global result
    if carry == N:
        result += 1
    elif carry < N and curCoin != 1000:
        limit = N//curCoin

        for i in range(limit+1):
            gen_nums(carry + curCoin*i, d[curCoin],N)

gen_nums(0,1,1000)

print(result)

