# 피보나치 수 2, B1, DP - DP 감 다시 잡기

n = int(input())

dp = [0, 1]

for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n])