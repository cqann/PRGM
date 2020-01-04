

n, m = [int(x) for x in input().split(" ")]
n_str = input().split(" ")
m_str = input().split(" ") 
q = int(input())
years = [int(input())-1 for x in range(q)]

for year in years:
    print(n_str[year%n] + m_str[year%m])