# 점프, S1, DP
from sys import stdin
board = []
n = int(stdin.readline())
for i in range(n):
    board.append(list(map(int, stdin.readline().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

res = 0
# dp[i][j] == (i,j)까지 올 수 있는 모든 경우의 수
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:       # 끝
            print(dp[i][j])
            break
        tmp = board[i][j]               # 현재 값
        if j + tmp < n:
            dp[i][j+tmp] += dp[i][j]    # 현재 값 만큼 이동
        if i + tmp < n:
            dp[i + tmp][j] += dp[i][j]
