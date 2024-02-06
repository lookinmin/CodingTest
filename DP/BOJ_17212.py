# 달나라 토끼... , S3
n = int(input())

coins = [1, 2, 5, 7]

dp = [100001] * (n + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, n + 1):
        if dp[i - coin] != 100001:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n])