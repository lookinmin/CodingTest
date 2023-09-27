# 아기 상어2, S2, BFS-완탐

from sys import stdin
from collections import deque

# 8방향 이동

res = 0

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]

def bfs(a, b):
    global res
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                elif graph[nx][ny] == 1:
                    res = max(res, visited[x][y])
                    return



for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            bfs(x, y)

print(res)