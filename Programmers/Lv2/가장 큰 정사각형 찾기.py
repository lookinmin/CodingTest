def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]

    res = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = board[i][j]
            elif board[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            res = max(dp[i][j], res)

    return res ** 2