# 현수막, S1, DFS

from sys import stdin
import sys

sys.setrecursionlimit(10**8)

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

m, n = map(int, stdin.readline().split())
graph = [[] for _ in range(m)]
for i in range(m):
    graph[i] = list(map(int, stdin.readline().split()))

cnt = 0

def dfs(a, b):
    graph[a][b] = 0

    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)