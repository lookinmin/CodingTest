# 창영이와 퇴근, G4, 다익스트라

from sys import stdin
import heapq

# 1,1 -> n,n

n = int(stdin.readline())

graph = [[] for _ in range(n)]
dist = [[int(1e9)] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(sx, sy):
    q = []
    heapq.heappush(q, (0, sx, sy))
    dist[sx][sy] = 0

    while q:
        distance, x, y = heapq.heappop(q)

        if dist[x][y] < distance:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                cost = max(distance, abs(graph[x][y] - graph[nx][ny]))

                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return dist

res = dijkstra(0, 0)
print(res[n-1][n-1])