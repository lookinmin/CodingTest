# 크림 파스타, S4
from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [[0, 1000000000]]

for i in range(1, n + 1):
    dp.append([max(dp[i-1][0], arr[i-1] - dp[i-1][1]), min(dp[i-1][1], arr[i-1])])

for i in range(1, n + 1):
    print(dp[i][0], end=" ")