# 도영이가 만든 맛있는 음식, S2, 백트래킹-완탐
# 재료 n개
# 신맛S, 쓴맛 B, S는 곱, B는 합

from sys import stdin
from itertools import combinations

n = int(stdin.readline())
arr = [list(map(int, input().split())) for _ in range(n)]
coms = [combinations(arr, i) for i in range(1, n+1)]
ans = 1000000000
for com in coms:
    for t in com:
        S, B = 1, 0
        for s, b in t:
            S *= s
            B += b
        ans = min(ans, abs(S-B))
print(ans)