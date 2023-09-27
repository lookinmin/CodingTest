# 데스 나이트, S1, 그래프

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[0]*n for _ in range(n)]
r1,c1,r2,c2 = map(int, stdin.readline().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


visited = [[0] * n for _ in range(n)]
def bfs(a, b):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if nx == r2 and ny == c2:
                    return visited[nx][ny] - 1
    return -1

print(bfs(r1, c1))