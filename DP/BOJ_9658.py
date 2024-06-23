# 돌 게임4, S2
n = int(input())

dp = [0] * 1001
# 1 -> sk
# 2 -> cy
# 3 -> sk
# 4 -> cy
# 5 -> cy
dp[1] = 0
dp[2] = 1
dp[4] = 1
dp[5] = 1
dp[6] = 1
dp[7] = 1

for i in range(8, n + 1):
    if 0 in (dp[i-1], dp[i-3], dp[i-4]):
        dp[i] = 1
    else:
        dp[i] = 0

print("SK" if dp[n] == 1 else "CY")