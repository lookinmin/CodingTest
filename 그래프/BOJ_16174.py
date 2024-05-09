# 점프왕 쩰리, S1
from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

visited = [[0] * n for _ in range(n)]
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        val = graph[x][y]

        if val == -1:
            print("HaruHaru")
            return

        for i in range(2):
            if i == 0:
                nx = x + val
                ny = y
            else:
                nx = x
                ny = y + val

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = 1

    print("Hing")

bfs()