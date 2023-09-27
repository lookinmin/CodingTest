# DFS & BFS, S2, 그래프
# 정점 번호가 작은 것 먼저

from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N + 1)
visited2 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    visited[v] = 1
    print(v, end = " ")
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)