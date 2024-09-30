def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0] * n for _ in range(n)]

    # 행렬 체인의 길이 2에서 n까지 반복
    for length in range(1, n):  # length는 행렬 곱셈 구간의 길이
        for i in range(n - length):  # i는 시작 행렬
            j = i + length  # j는 마지막 행렬
            dp[i][j] = float('inf')
            for k in range(i, j):  # i에서 j사이의 k번째에서 나눔
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]
