# 전쟁 - 전투, S1, 그래프

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(m)]
visited = [[0] * n for _ in range(m)]
for i in range(m):
    graph[i] = list(stdin.readline().rstrip())

dx = [-1, 1, 0 ,0]
dy = [0, 0 ,-1, 1]

def bfs(x,y):
    q = deque()
    cnt = 1
    q.append([x,y])
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == graph[a][b]:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    cnt += 1

    return cnt

W, B = 0,0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'B' and not visited[i][j]:
            tmpB = bfs(i,j)

            B += (tmpB**2)
        elif graph[i][j] == 'W' and not visited[i][j]:
            tmpW = bfs(i,j)

            W += (tmpW ** 2)

print(W, B)