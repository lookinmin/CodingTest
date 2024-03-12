# 농장 관리, G4, BFS
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

check = []

def bfs(a, b, check):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    now = [(a, b)]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] > graph[x][y]:
                    return 0
                elif graph[x][y] == graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    now.append((nx, ny))
        check += now
    return 1

res = 0
for i in range(n):
    for j in range(m):
        if (i,j) not in check:
            visited = [[0] * m for _ in range(n)]
            res += bfs(i, j, check)

print(res)
