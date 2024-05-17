# 그대, 그머가 되어, S2
from sys import stdin
from collections import deque

a, b = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

res = int(1e9)

def bfs(start):
    global res
    q = deque()
    q.append([start, 0])
    visited[start] = 1
    
    while q:
        x, cnt = q.popleft()
        
        if x == b:
            res = min(cnt, res)
            
        for node in graph[x]:
            if not visited[node]:
                q.append([node, cnt + 1])
                visited[node] = 1

bfs(a)
print(-1 if res == int(1e9) else res)