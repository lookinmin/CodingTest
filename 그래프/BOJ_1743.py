# 음식물 피하기, S1, 그래프

from sys import stdin
from collections import deque

n, m , k = map(int, stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int,stdin.readline().split())
    graph[r-1][c-1] = 1

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    res = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                res += 1
    return res
tmp_max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = (bfs(i,j))
            tmp_max = max(tmp_max, ans)
print(tmp_max)