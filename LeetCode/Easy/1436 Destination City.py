class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        visited = [0] * len(paths)
        res = ""

        def dfs(std):
            nonlocal res
            nxt = False

            for i in range(len(paths)):
                if visited[i] == 0 and paths[i][0] == std:
                    visited[i] = 1
                    dfs(paths[i][1])
                    nxt = True
            
            if not nxt:
                res = std
        
        dfs(paths[0][0])
        return res
        
        