# 민준이와 마산 그리고 건우, G4, 다익스트라

from sys import stdin
import heapq

V, e, p = map(int, stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(V+1)]

# start = 1, end = v, 건우 = p
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dikjstra(s):
    q = []
    heapq.heappush(q, (0, s))

    dist = [INF] * (V + 1)
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for v, w in graph[now]:
            cost = w + distance
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

    return dist

if dikjstra(1)[V] == dikjstra(1)[p] + dikjstra(p)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
