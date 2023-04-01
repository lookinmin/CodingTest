# 백도어, G5, 다익스트라

from sys import stdin
import heapq
import sys
INF = sys.maxsize

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        distance,now = heapq.heappop(q)
        if dist[now] < distance:
            continue

        for v, w in graph[now]:
            cost = w + distance
            if cost < dist[v] and views[v] == 0:        # 해당 넘버의 노드가 방문가능
                dist[v] = cost
                heapq.heappush(q, (cost, v))


n, m = map(int,stdin.readline().split())
views = list(map(int,stdin.readline().split()))
views[-1] = 0

graph =[[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dijkstra(0)

if dist[n-1] == INF:
    print(-1)
else:
    print(dist[n-1])