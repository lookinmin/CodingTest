# 공주님을 구해라, G5, 그래프

from sys import stdin
from collections import deque

# start  = (0,0)

n, m, t = map(int,stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

sword = 1000000

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

def bfs(a, b):
    global sword

    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        if graph[x][y] == 2:        # 칼먹으면 공주한테 직진
            sword = n-1-x + m-1-y + visited[x][y] - 1

        if x == n-1 and y == m-1:
            return min(visited[x][y]-1, sword)      # 칼 먹고 가는게 빠른지 그냥 가는게 빠른지


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return sword

res = bfs(0,0)
if res > t:
    print("Fail")
else:
    print(res)


