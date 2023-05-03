# 녹색 옷 입은 애가 젤다지?, G4, 다익스트라

from sys import stdin
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost ,x ,y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print("Problem {}: {}".format(cnt, dist[x][y]))
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                new_cost = cost + graph[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

cnt = 1

while 1:
    n = int(stdin.readline())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, stdin.readline().split()))

    dist = [[int(1e9)]*n for _ in range(n)]
    dijkstra()
    cnt += 1

