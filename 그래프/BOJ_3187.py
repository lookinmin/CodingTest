# 양치기 꿍, S1, 그래프
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(str, stdin.readline().rstrip()))

visited = [[0] * m for _ in range(n)]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    wolf, sheep = 0, 0
    if graph[a][b] == 'v':
        wolf = 1
    elif graph[a][b] == 'k':
        sheep = 1

    visited[a][b] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == '.':
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 'v':
                    q.append([nx, ny])
                    wolf += 1
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 'k':
                    q.append([nx, ny])
                    sheep += 1
                    visited[nx][ny] = 1
    if wolf < sheep:
        return [sheep, 0]
    else:
        return [0, wolf]

res = [0, 0]
for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and not visited[i][j]:
            tmp = bfs(i, j)
            res[0] += tmp[0]
            res[1] += tmp[1]

print(*res)