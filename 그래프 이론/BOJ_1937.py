# 욕심쟁이 판다, G3, DFS

from sys import stdin
import sys
sys.setrecursionlimit(10**8)
from collections import deque
# 최대한 많은 칸 이동하게

n = int(stdin.readline())
graph = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(a, b):
    if visited[a][b]:
        return visited[a][b]
    visited[a][b] = 1

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[a][b] < graph[nx][ny]:
            visited[a][b] = max(visited[a][b], dfs(nx, ny) + 1)
    return visited[a][b]


res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))

print(res)
