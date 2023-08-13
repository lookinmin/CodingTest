# 쉬운 최단거리, S1, BFS

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

# 시작점이 2, 각 1까지의 거리 측정

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
        if graph[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    print(*visited[i])

