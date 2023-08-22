# 아기 상어, G3, 구현

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n)]


for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

shark = 2
pos = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    tmp = []        # 먹이 위치

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph[a][b]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] != 0 and graph[a][b] > graph[nx][ny]:      # 먹을 수 있음
                    visited[nx][ny] = visited[x][y] + 1
                    tmp.append((visited[nx][ny] - 1, nx, ny))
                elif graph[a][b] == graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return sorted(tmp, key=lambda x: (x[0], x[1], x[2]))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)

x, y = pos
size = [2, 0]       # 시작 크기2, 먹이 0

cnt = 0

while 1:
    graph[x][y] = size[0]       # 현 위치 값을 시작 사이즈인 2로 바꿔줌
    tmp = deque(bfs(x, y))      # 현 위치부터 bfs 수행해 먹이위치 찾음

    if not tmp:  # tmp 내부의 값을 전부 꺼냈으면
        break

    step, nx, ny = tmp.popleft()
    cnt += step

    size[1] += 1

    if size[0] == size[1]:  # 크기 만큼 먹이 먹었으면,
        size[0] += 1
        size[1] = 0

    graph[x][y] = 0
    x, y = nx, ny

print(cnt)




