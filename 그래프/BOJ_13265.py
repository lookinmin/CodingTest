from sys import stdin
from collections import deque

def is_bipartite(graph):
    colors = [0] * (len(graph))  # 0: 미방문, 1: 색1, 2: 색2
    
    def bfs(start):
        q = deque([start])
        colors[start] = 1  # 시작 노드의 색상은 중요하지 않음
        
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = 3 - colors[node]  # 1 -> 2, 2 -> 1
                    q.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True
    
    for node in range(1, len(graph)):
        if colors[node] == 0:
            if not bfs(node):
                return False
    return True

T = int(stdin.readline())

for _ in range(T):
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print("possible" if is_bipartite(graph) else "impossible")