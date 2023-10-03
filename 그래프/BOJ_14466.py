# 소가 길을 건너간 이유6, G4, 그래프

from sys import stdin
from collections import deque

n, k, r = map(int, stdin.readline().split())

graph = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
for _ in range(r):
    r1, c1, r2, c2 = map(int, stdin.readline().split())
    r1 = r1-1
    c1 = c1-1
    r2 = r2-1
    c2 = c2-1

    graph[r1][c1].append((r2, c2))
    graph[r2][c2].append((r1, c1))

cow = list()
for _ in range(k):
    r, c = map(int, stdin.readline().split())
    cow.append((r-1,c-1))

def bfs(a, b):
    q = deque()
    q.append((a, b))

    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if (nx,ny) in graph[x][y]:  # 다리가 있음
                    continue    # pass, 이어지지 않은 소의 쌍만 확인해야함
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = 1


for i, c in enumerate(cow):
    visited = [[0] * n for _ in range(n)]

    bfs(c[0], c[1])
    for r2, c2 in cow[i + 1: ]:
        if not visited[r2][c2]:
            cnt += 1

print(cnt)