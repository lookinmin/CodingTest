# 탈출, G4, BFS

# S->D
from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())

graph = [[] for _ in range(r)]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    graph[i] = list(stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

q = deque()

def bfs(x, y):
    while q:
        a, b = q.popleft()

        if graph[x][y] == 'S':
            return visited[x][y]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<r and 0<=ny<c:
                # 현재 고슴도치 위치에서 다음꺼 방문 가능
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[a][b] == 'S':
                    graph[nx][ny] = 'S'
                    q.append([nx, ny])
                    visited[nx][ny] = visited[a][b] + 1
                # 현재 물 위치에서 다음꺼 방문 가능
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[a][b] == '*':
                    graph[nx][ny] = '*'
                    q.append([nx, ny])
    return "KAKTUS"

a, b = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q.append([i, j])        # 고슴도치 위치를 먼저 넣어줌
        elif graph[i][j] == 'D':
            a, b = i, j

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append([i, j])        # 후에, 물 위치를 큐에 넣어줌

print(bfs(a, b))

