class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[i , j] = i~j에서 숫자를 맞추기 위해 필요한 최소 비용

        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                dp[start][end] = float('inf')

                for k in range(start, end):
                    worst = k + max(dp[start][k - 1], dp[k + 1][end])
                    dp[start][end] = min(dp[start][end], worst)
        
        return dp[1][n]