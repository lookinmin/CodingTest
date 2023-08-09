# 이동하기, S2, DP - 재시도

from sys import stdin

n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

# dp[0][0] = graph[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


print(dp[n][m])