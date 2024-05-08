# 한윤정...사먹는데, S4
from sys import stdin
from itertools import combinations
n, m = map(int, stdin.readline().split())
res = 0

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, stdin.readline().split())
    dp[x][y] = 1
    dp[y][x] = 1

for comb in list(combinations(range(1, n + 1), 3)):
    a, b, c = comb
    if dp[a][b] or dp[a][c] or dp[b][c]:
        continue
    res += 1

print(res)