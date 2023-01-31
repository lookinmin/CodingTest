# 거스름돈, S5, DP
# 돈은 2,5

n = int(input())
dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
for i in range(10, n+1):
    dp.append(dp[i-5] + 1)

print(dp[n])
