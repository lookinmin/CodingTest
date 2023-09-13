# 주난의 난, G4, 다익스트라, 0-1 BFS

# * = 주난, # = 초코바

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
x1,y1,x2,y2 = map(int, stdin.readline().split())
x1 = x1-1
y1 = y1-1
x2 = x2-1
y2 = y2-1

for i in range(n):
    graph[i] = list(stdin.readline().rstrip())
INF = int(1e9)
dist = [[INF]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a,b):
    q = deque()
    dist[a][b] = 0
    q.append([x1, y1])

    while q:
        x ,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and dist[nx][ny] == INF:
                if graph[nx][ny] == '0':
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                else:           # 벽이면 +1 하면 됨
                    q.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

bfs(x1, y1)

print(dist[x2][y2])