# 특정한 최단경로, G4, 그래프-다익스트라
# 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(e):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, stdin.readline().split())

def dijksta(s):
    dist = [INF] * (n + 1)
    q = []
    dist[s] = 0
    heapq.heappush(q, (0,s))

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for v, w in graph[now]:
            cost = w + distance
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))
    return  dist


# 두 점을 지나야 함
# 1. 1 -> v1 -> v2 -> N
# 2. 1 -> v2 -> v1 -> N
original = dijksta(1)
start_v1 = dijksta(v1)
start_v2 = dijksta(v2)

path_v1 = original[v1] + start_v1[v2] + start_v2[n]
path_v2 = original[v2] + start_v2[v1] + start_v1[n]
res = min(path_v1, path_v2)

if res < INF:
    print(res)
else:
    print(-1)
