# 행렬 곱셈 순서, G3, DP

from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    r, c = map(int, stdin.readline().split())
    arr.append([r,c])

dp = [[0] * n for _ in range(n)]
INF = int(1e9)
for i in range(1, n):       # 몇번째 대각선인가
    for j in range(0, n-i): # 대각선에서 몇번째 열인지
        if i == 1:          # 차이가 1인 열
            dp[j][j+i] = arr[j][0]*arr[j][1]*arr[j+i][1]
            continue

        dp[j][j+i] = INF

        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1])

print(dp[0][n-1])