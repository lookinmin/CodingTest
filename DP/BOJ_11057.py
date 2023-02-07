# 오르막수, S1, DP

n = int(input())
dp = [1] * 10

# 맨 뒤에 오는 수 기준, dp[i] = dp[i-1] + dp[i]

for i in range(n-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)
