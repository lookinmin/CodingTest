class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        visited = [0] * numCourses
        
        order = [] # 위상 정렬 그래

        def dfs(v):
            if visited[v] == 1:
                return False    # cycle
            if visited[v] == 2:
                return True     # 방문완료

            visited[v] = 1

            for node in graph[v]:
                if not dfs(node):
                    return False
            
            visited[v] = 2
            order.append(v)
            return True
        
        for node in range(numCourses):
            if not visited[node]:
                if not dfs(node):
                    return []
        return order[::-1]