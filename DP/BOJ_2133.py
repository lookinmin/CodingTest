# 타일 채우기, G4, DP

n = int(input())

dp = [0] * 31

dp[1] = 0
dp[2] = 3
# dp[3] = 0
# dp[4] = dp[2] ** 2 + 2
# dp[6] = dp[4] * dp[2] + dp[2]*2 + 2
#         # dp[2]**3 + dp[2]*2 + 2
# dp[8] = dp[6] * dp[2] + dp[4]*2+dp[2]*2+2
# 홀수는 0 짝수는 이전 짝수 * 2 + 2

for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] += dp[i-2]*dp[2]
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] += 2



print(dp[n])
