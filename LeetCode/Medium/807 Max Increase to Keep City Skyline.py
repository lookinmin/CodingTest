class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # 북쪽에서 볼 때
        n = len(grid)
        north = []
        for i in range(n):
            tmp = 0
            for j in range(n):
                tmp = max(tmp, grid[j][i])
            north.append(tmp)

        # 서쪽에서 볼 때
        west = []
        for i in range(n):
            tmp = 0
            for j in range(n):
                tmp = max(tmp, grid[i][j])
            west.append(tmp)
        
        newGrid = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                newGrid[i][j] = min(west[i], north[j])
        
        res = 0
        for i in range(n):
            for j in range(n):
                res += (newGrid[i][j] - grid[i][j])
        
        return res
