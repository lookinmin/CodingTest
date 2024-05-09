# 철벽보안, S4
from sys import stdin
from collections import defaultdict
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    oneKey = list(map(str, stdin.readline().split()))
    twoKey = list(map(str, stdin.readline().split()))
    message = list(map(str, stdin.readline().split()))

    dic = defaultdict(int)
    for i in range(n):
        dic[i] = twoKey.index(oneKey[i])

    rev_dic = defaultdict(int)
    for a, b in dic.items():
        rev_dic[b] = a

    res = ['']*n
    for a, b in rev_dic.items():
        res[b] = message[a]

    print(*res)
