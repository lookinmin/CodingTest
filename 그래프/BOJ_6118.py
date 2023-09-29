# 숨바꼭질, S1, BFS

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
# start = 1

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * (n+1)
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        node = q.popleft()

        for v in graph[node]:
            if not visited[v]:
                visited[v] = visited[node] + 1
                q.append(v)

bfs(1)
num = 0
dist = 0
cnt = 0

for i in range(1, n+1):
    if visited[i] > dist:
        dist = visited[i]
        num = i

print(num, dist-1, visited.count(dist))