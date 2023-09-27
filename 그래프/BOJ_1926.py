# 그림, S1, 그래프
# bfs

from sys import stdin
from collections import deque

n,m = map(int, stdin.readline().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

def bfs(a, b):
    cnt = 1
    q= deque()
    q.append([a,b])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    cnt += 1
    return cnt

res_cnt = 0
res_max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            res_cnt += 1
            res_max = max(res_max, bfs(i, j))

print(res_cnt)
print(res_max)