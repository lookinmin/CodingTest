class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return[1]
        elif rowIndex == 1:
            return [1, 1]
        dp = [[] for _ in range(rowIndex + 1)]
        dp[0] = [1]
        dp[1] = [1, 1]
        dp[2] = [1, 2, 1]
        
        for i in range(3, rowIndex + 1):
            tmp = []
            for j in range(0, len(dp[i-1]) - 1):
                tmp.append(dp[i-1][j] + dp[i-1][j + 1])
            dp[i] = [1] + tmp + [1]
        
        return dp[rowIndex]