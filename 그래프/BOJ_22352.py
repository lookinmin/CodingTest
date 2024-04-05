# 항체 인식, G5
from sys import stdin
from collections import deque
import copy

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

after = [[] for _ in range(n)]

for i in range(n):
    after[i] = list(map(int, stdin.readline().split()))

def bfs(sx, sy, value):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = value
    tmp = graph[sx][sy]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        graph[x][y] = value

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == tmp:
                visited[nx][ny] = value
                q.append([nx, ny])

value = 0
visited = [[0] * m for _ in range(n)]
flag = True

for i in range(n):
    for j in range(m):
        if graph[i][j] != after[i][j] and flag:
            flag = False
            value = after[i][j]
            bfs(i, j, value)

if flag:
    print('YES')
else:
    for i in range(n):
        for j in range(m):
            if graph[i][j] != after[i][j]:
                print("NO")
                exit(0)

    print("YES")