# S4, 점프왕 쩰리

from sys import stdin
from collections import deque

n = int(stdin.readline())
board = [[0] * n for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))
dx = [1, 0]
dy = [0, 1]
visited = [[0] * n for _ in range(n)]

def bfs(a, b):
    visited[a][b] = 1
    q = deque()
    q.append([a, b])

    while q:
        x, y = q.popleft()

        if board[x][y] == -1:
            return "HaruHaru"

        cnt = board[x][y]

        for i in range(2):
            nx = x + dx[i] * cnt
            ny = y + dy[i] * cnt

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])

    return "Hing"


print(bfs(0, 0))