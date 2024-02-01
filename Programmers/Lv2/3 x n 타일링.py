def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11  # 3 ** 2 + 2 ** 1

    if n % 2 != 0:
        return 0
    else:
        for i in range(6, n + 1, 2):
            dp[i] = 3 * dp[i - 2] + 2
            for j in range(i - 4, -1, -2):
                dp[i] += dp[j] * 2
            dp[i] %= 1000000007

    return dp[n]