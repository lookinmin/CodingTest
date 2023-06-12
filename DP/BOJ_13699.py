# 점화식, S4, DP

n = int(input())

dp = [0] * 36

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5

if n > 3:
    for i in range(4, n+1):
        for j in range(i):
            dp[i] += (dp[j] * dp[i-j-1])


print(dp[n])