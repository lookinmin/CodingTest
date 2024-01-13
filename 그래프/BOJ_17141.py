# 연구소 2, G4, BFS

from collections import deque
from sys import stdin
from itertools import combinations

n, M = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]
virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j])

def bfs(node):
    q = deque(node)
    visited = [[-1] * n for _ in range(n)]

    cnt = 0

    for a,b in q:
        visited[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1 and graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                cnt = max(cnt, visited[x][y] + 1)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return int(1e9)
    return cnt

answer = int(1e9)
for v in combinations(virus, M):
    answer = min(bfs(v), answer)

if answer == int(1e9):
    print(-1)
else:
    print(answer)