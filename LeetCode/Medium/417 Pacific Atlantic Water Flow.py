class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        # 뭐든 상관없이 [0, m-1], [n-1, 0] 은 가능

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        p_visited = [[0] * m for _ in range(n)]
        a_visited = [[0] * m for _ in range(n)]

        def dfs(x, y, visited):
            visited[x][y] = 1
            now = heights[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny, visited)
        
        for i in range(n):
            dfs(i, 0, p_visited)
            dfs(i, m-1, a_visited)
        
        for j in range(m):
            dfs(0, j, p_visited)
            dfs(n-1, j, a_visited)

        res = []
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] == 1 and a_visited[i][j] == 1:
                    res.append([i, j])
        return res