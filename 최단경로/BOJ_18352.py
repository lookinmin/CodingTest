# 특정 거리의 도시찾기, S2, 다익스트라

from sys import stdin
import heapq
# 모든 도시의 거리는 1

n,m,k,x  = map(int, stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n+1)

for _ in range(m):
    s, e  = map(int, stdin.readline().split())
    graph[s].append((e, 1))

def dijkstra(s):
    q = []
    dist[s] = 0
    heapq.heappush(q, (0,s))

    while q:
        distance, now = heapq.heappop(q)

        if distance > dist[now]:
            continue

        for v, w in graph[now]:
            cost = distance + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(x)
res = []
flag = True
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        flag = False

if flag:
    print(-1)

