# 침투, S2, 그래프

from sys import stdin
from collections import deque

# [0]에서 시작된 탐색이 [n-1]에 전달되는지

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

# 0이 흰색, 1이 검은색
v = []
for i in range(m):
    if graph[0][i] == 0:
        v.append([0, i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v):
    q = deque(v)

    for a, b in q:
        visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != 1:
                q.append([nx, ny])
                visited[nx][ny] = 1

bfs(v)
flag = False
for i in range(m):
    if visited[n-1][i] != 0:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
