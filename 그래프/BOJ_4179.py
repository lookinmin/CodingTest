# 불!, G4, BFS

from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())

graph = [[] for _ in range(r)]

for i in range(r):
    graph[i] = list(stdin.readline().rstrip())

fire_q = deque()
jihun_q = deque()

fire_visited = [[-1] * c for _ in range(r)]
jihun_visited = [[-1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fire_visited[i][j] = 0
            fire_q.append((i,j))
        elif graph[i][j] == 'J':
            jihun_visited[i][j] = 0
            jihun_q.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if fire_visited[nx][ny] == -1 and graph[nx][ny] != '#':
                    fire_visited[nx][ny] = fire_visited[x][y] + 1
                    fire_q.append((nx, ny))

    while jihun_q:
        x ,y = jihun_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if jihun_visited[nx][ny] == -1 and graph[nx][ny] != '#':
                    if fire_visited[nx][ny] == -1 or fire_visited[nx][ny] > jihun_visited[x][y] + 1:
                        # 이미 불이 붙어 있지 않아야하고, 다음에 방문할 곳이 불이 붙어있어야 하지 않음
                        jihun_visited[nx][ny] = jihun_visited[x][y] + 1
                        jihun_q.append((nx, ny))
            else:
                return jihun_visited[x][y] + 1      # 이 시간에 탈출가능(모서리에 위치함)
    return "IMPOSSIBLE"

print(bfs())


