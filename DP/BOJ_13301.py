# 타일 장식물, S5, DP

from sys import stdin

n = int(stdin.readline())
dp = [0, 1, 1, 2]

for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] * 4 + dp[n-1] * 2)