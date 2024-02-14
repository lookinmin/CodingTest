# 양 한마리... 양 두마리... , S2

from sys import stdin
from collections import deque

T = int(stdin.readline())
def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == '#':
                    q.append([nx, ny])
                    visited[nx][ny] = 1

for _ in range(T):
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        graph[i] = list(stdin.readline().rstrip())

    res = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and graph[x][y] == '#':
                bfs(x, y)
                res += 1

    print(res)
