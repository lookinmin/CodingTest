# 로또, S2, 백트래킹
# 1~49 중 6개
from sys import stdin
from itertools import combinations

while True:
    a = list(map(int, stdin.readline().split()))
    k = a[0]
    s = a[1:]
    if k == 0:
        break
    for i in list(combinations(s, 6)):
        print(*i)
    print()


# dfs를 이용한 풀이

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=" ")
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i+1, depth + 1)

combi = [0 for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()