# 택배 배송, G5, 다익스트라

from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
# 1에서 시작 n에 도착
INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0,s))        # 값, 노드
    dist[s] = 0


    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue

        for v, w in graph[now]:
            cost = distance + w

            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(1)

print(dist[n])