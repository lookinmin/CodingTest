# Coins, G5, DP-knapsack problem

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())

    dp = [0] * (m+1)
    dp[0] = 1
    # dp[i] = i원 동전을 이용해 만들 수 있는 방법의 수
    # 동전 종류가 1, 2, 3 일때 6원을 만드는 방법
    for i in range(n):
        for j in range(coins[i], m + 1):
            # print(j)        # 1원 ~ 6원, 2원 ~ 6원, 3원 ~ 6원
            dp[j] += dp[j - coins[i]]

    # i = 0, j = 1~6, coins[0] = 1
    # dp[1] += dp[1-1](1)
    # dp[2] += dp[2-1](1)
    # dp[3] += dp[3-1](1)
    # ... -> dp[0] ~ dp[6] 까지 전부 1
    # i = 1, j = 2~6, coins[1] = 2
    # dp[2] += dp[2-2](1 + 1)
    # dp[3] += dp[3-2](1 + 1)
    # dp[4] += dp[4-2](1 + 2)
    # ... -> dp[0] ~ dp[6] = 1, 1, 2, 2, 3, 3, 4
    # i = 2, j = 3~6, coins[2] = 3
    # dp[3] += dp[3-3](2 + 1)
    # dp[4] += dp[4-3](3 + 1)
    # dp[5] += dp[5-3](3 + 2)
    # dp[6] += dp[6-3](4 + 3)
    # -> dp[0] ~ dp[6] = 1, 1, 2, 3, 4, 5, 7
    # 답은 7(1원짜리 6개, 2원짜리 3개, 3원짜리 2개, 1원 2개 + 2원 2개, 1원 4개 + 2원 1개, 1원 3개 + 3원 1개, 1원 1개 2원 1개 3원 1개 )
    print(dp[m])