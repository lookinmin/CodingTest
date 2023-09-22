# 너비 우선 탐색2, S2, BFS

from sys import stdin
# 인접정점 내림차순 방문
from collections import deque

n, m, r = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

cnt = 1

def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        node = q.popleft()

        for v in graph[node]:
            if visited[v] == 0:
                cnt += 1
                visited[v] = cnt
                q.append(v)

bfs(r)

print(*visited[1:], sep="\n")