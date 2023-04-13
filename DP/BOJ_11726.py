# 2xn 타일링, S3, DP

n = int(input())

dp=[0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 3       # 막대를 3개 사용
dp[4] = 5
dp[5] = 8

# dp[n] = dp[n-2] + dp[n-1]

for i in range(6, 1001):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)

