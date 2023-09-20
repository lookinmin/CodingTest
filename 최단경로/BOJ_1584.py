# 게임, G5, 최단경로, 0-1 BFS
from sys import stdin
from collections import deque
import heapq

# 0,0 -> 500,500

n = int(stdin.readline())
# 위험
danger = []
for i in range(n):
    danger.append(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
# 죽음
death = []
for i in range(m):
    death.append(list(map(int, stdin.readline().split())))

# 위험에서 움직일때마다 +1
# 죽음은 움직일 수 없음

graph = [[0] * 501 for _ in range(501)]

for k in range(n):
    for i in range(min(danger[k][0], danger[k][2]), max(danger[k][0], danger[k][2]) + 1):
        for j in range(min(danger[k][1], danger[k][3]), max(danger[k][1], danger[k][3]) + 1):
            graph[i][j] = 1
for k in range(m):
    for i in range(min(death[k][0], death[k][2]), max(death[k][0], death[k][2]) + 1):
        for j in range(min(death[k][1], death[k][3]), max(death[k][1], death[k][3]) + 1):
            graph[i][j] = 2

dist = [[int(1e9)] * 501 for _ in range(501)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(a, b):
    dist[a][b] = 0
    q = []
    heapq.heappush(q,(0,a,b))

    while q:
        value, x, y = heapq.heappop(q)

        if value > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<=500 and 0<=ny<=500 and graph[nx][ny] != 2:
                cost = 0
                if graph[nx][ny] == 1:
                    cost += 1
                if dist[nx][ny] > value + cost:
                    dist[nx][ny] = value + cost
                    heapq.heappush(q, (value + cost, nx, ny))
dijkstra(0, 0)
print(dist[500][500] if dist[500][500] != int(1e9) else -1)