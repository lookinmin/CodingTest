# 헌내기는 친구가 필요해, S2, BFS

from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def bfs(a, b):
    global cnt
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != 'X':
                if graph[nx][ny] == 'P':
                    cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            bfs(i, j)

print(cnt if cnt > 0 else 'TT')

