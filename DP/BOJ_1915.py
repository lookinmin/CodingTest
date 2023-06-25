# 가장 큰 정사각형, G4, DP

from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

dp = [[0] * m for _ in range(n)]
# 1 2
# 3 4 에서 1,2,3 중 최소인 값의 +1이 최대크기를 가지는 정사각형
res = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        res = max(dp[i][j], res)

print(res ** 2)

