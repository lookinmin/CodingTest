# MooTube, G5, 그래프

from sys import stdin
from collections import deque

n, q = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, usado = (map(int, stdin.readline().split()))
    graph[a].append((b, usado))
    graph[b].append((a, usado))



for _ in range(q):
    k, v = map(int, stdin.readline().split())
    visited = [0] * (n + 1)
    visited[v] = 1

    q = deque()
    q.append((v, float('inf')))

    res = 0
    while q:
        v, usado = q.popleft()
        for node, value in graph[v]:
            value = min(usado, value)
            if value >= k and not visited[node]:
                res += 1
                q.append((node, value))
                visited[node] = 1
    print(res)