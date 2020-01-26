
t = int(input())
dic = {}
for i in range(t):
    a,b,c = [int(x) for x in input().split(" ")]
    if (a,b,c) in dic:
        print(dic[(a,b,c)])
    else:
        if a + b + c == 180 and a != 0 and b != 0 and c != 0:
            dic[(a,b,c)] = "YES"
            dic[(b,c,a)] = "YES"
            dic[(c,a,b)] = "YES"
            dic[(b,a,c)] = "YES"
            dic[(a,c,b)] = "YES"
            dic[(c,b,a)] = "YES"
            print("YES")
        else:
            dic[(a,b,c)] = "NO"
            dic[(b,c,a)] = "NO"
            dic[(c,a,b)] = "NO"
            dic[(b,a,c)] = "NO"
            dic[(a,c,b)] = "NO"
            dic[(c,b,a)] = "NO"
            print("NO")
