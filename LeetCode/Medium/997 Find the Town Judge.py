from collections import deque
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b in trust:
            graph[a].append(b)
        
        candidates = []
        for num in range(1, n + 1):
            if len(graph[num]) == 0:
                candidates.append(num)
        
        dist = [0] * (n + 1)

        def bfs(n):
            visited = set()
            q = deque()
            q.append(n)

            while q:
                node = q.popleft()

                for adj in graph[node]:
                    if adj not in visited:
                        visited.add(adj)
                        dist[adj] += 1
            return
        
        for i in range(1, n + 1):
            if i not in candidates:
                bfs(i)
        
        for cand in candidates:
            if dist[cand] == n - 1:
                return cand
        
        return -1
