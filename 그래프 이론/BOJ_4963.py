# 섬의 개수, S2, 그래프 이론 - DFS & BFS
# BFS

from sys import stdin
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    graph[x][y] = 0                     # 방문한 곳을 바다로 -> 다시 안 돌아가게끔
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])


while 1:
    w, h = map(int, stdin.readline().split())
    if w == h == 0:
        break
    graph = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        graph[i] = list(map(int, stdin.readline().split()))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
