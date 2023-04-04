# 간선 이어가기2, G5, 다익스트라
# 무방향 그래프

import heapq
from sys import stdin

n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dikjstra(s):
    q = []
    heapq.heappush(q, (0,s))
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:        # 이미 작으니까 갱신할 필요가 없음
            continue

        for v,w in graph[now]:
            cost = distance + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q,(cost, v))

s, t = map(int, stdin.readline().split())
dikjstra(s)
print(dist[t])


