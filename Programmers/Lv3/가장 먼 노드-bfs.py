from collections import deque
from collections import Counter

def solution(n, edge):
    visited = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    def bfs():
        q = deque()
        q.append(1)
        visited[1] = 0
        
        while q:
            v = q.popleft()
            
            for node in graph[v]:
                if visited[node] == -1:
                    visited[node] = visited[v] + 1
                    q.append(node)
        return
    
    bfs()
    maxDist = max(visited[1:])
    counter = Counter(visited[1:])
    res = counter[maxDist]
    return res