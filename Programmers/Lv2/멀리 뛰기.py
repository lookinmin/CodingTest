def solution(n):
    answer = 0

    if n < 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    # 규칙찾기
    # dp[3] = dp[1] + dp[2]
    # dp[4] = dp[2] + dp[3]
    # ...
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[n] % 1234567

    return answer


# 간단 DP