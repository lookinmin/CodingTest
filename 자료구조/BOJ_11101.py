# 꿍의 여친 만들기, S2
from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    one = stdin.readline().rstrip()
    two = stdin.readline().rstrip()
    
    dic = dict()
    for val in one.split(","):
        a, b = val.split(':')[0], val.split(':')[1]
        dic[a] = int(b)

    comb = []
    
    for val in two.split('|'):
        tmp = val.split('&')
        temp = []
        for a in tmp:
            temp.append(a)
        comb.append(temp)
    
    res = int(1e9)
    for c in comb:
        k = 0
        for val in c:
            k = max(k, dic[val])
        res = min(res, k)
    
    print(res)