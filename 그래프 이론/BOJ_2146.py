# 다리 만들기, G3, BFS
# BFS()를 2번 수행해야 하는 문제
# 각 섬끼리의 구분을 위해 1번
# 섬에서 섬까지의 거리를 구하기위해 1번

from sys import stdin
from collections import deque

n = int(stdin.readline())

graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = int(1e9)
cnt = 1

def bfs(x ,y):          # 섬 구분하기
    global cnt
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    graph[x][y] = cnt

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                graph[nx][ny] = cnt
                q.append([nx, ny])

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            bfs(i, j)
            cnt += 1

# for i in range(n):
#     print(*graph[i])

def makeBridge(v):
    global res
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:            # 현재 탐색하고 있는 섬과 같은 위치
                q.append([i,j])
                dist[i][j] = 0              # 최소거리로

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != v:        # 탐색하다가 다른 땅 만남
                res = min(res, dist[x][y])                      # 최소값 변경
                return
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:       # 바다임 -> dist += 1 하면서 탐색
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


for i in range(1, cnt):     #각 번호가 다른 대륙들을 탐색하면서
    makeBridge(i)

print(res)