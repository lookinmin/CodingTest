# 해킹, G4, 다익스트라
# 단방향 그래프

from sys import stdin
import heapq

T = int(stdin.readline().rstrip())
INF = int(1e9)

def dijsktra(s, graph, dist):
    q = []
    heapq.heappush(q, (0, s))
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


for _ in range(T):
    n, d, c = map(int, stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)

    for _ in range(d):
        a, b, s = map(int, stdin.readline().split())
        graph[b].append([a, s])

    dijsktra(c, graph, dist)

    cnt, res = 0, 0
    for i in dist:
        if i != INF:
            cnt += 1
            res = max(res, i)

    print(cnt, res)