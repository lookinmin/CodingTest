# 불, G4, BFS

from sys import stdin
from collections import deque

T = int(stdin.readline())

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(w, h, f_q, s_q, f_visited, s_visited, graph):
    while f_q:
        a, b = f_q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] != '#' and not f_visited[nx][ny]:
                f_visited[nx][ny] = f_visited[a][b] + 1
                f_q.append((nx, ny))

    while s_q:
        a, b = s_q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] != '#' and not s_visited[nx][ny]:
                    if not f_visited[nx][ny] or s_visited[a][b] + 1 < f_visited[nx][ny]:
                        s_visited[nx][ny] = s_visited[a][b] + 1
                        s_q.append((nx, ny))
            else:
                return s_visited[a][b]
    return "IMPOSSIBLE"

for _ in range(T):
    w, h = map(int, stdin.readline().split())
    graph = [[] for _ in range(h)]
    s_visited = [[0] * w for _ in range(h)]
    f_visited = [[0] * w for _ in range(h)]

    s_q = deque()
    f_q = deque()

    for i in range(h):
        graph[i] = list(stdin.readline().rstrip())

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                s_q.append((i, j))
                s_visited[i][j] = 1
            if graph[i][j] == '*':
                f_q.append((i, j))
                f_visited[i][j] = 1

    print(bfs(w, h, f_q, s_q, f_visited, s_visited, graph))


