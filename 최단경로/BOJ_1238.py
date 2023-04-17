# 파티, G3, 다익스트라

from sys import stdin
import heapq

# 왕복임, 단방향

n,m,x = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)


for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(s):
    q = []
    dist = [INF] * (n + 1)          # 가는거랑 오는거 따로 계산
    heapq.heappush(q, (0,s))
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for v, w in graph[now]:
            cost = w + distance
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q,(cost, v))
    return dist         # 거리를 계산한 리스트를 리턴

res = 0
for i in range(1, n+1):
    go = dijkstra(i)        # 현재 노드에서 출발
    back = dijkstra(x)      # x로 부터 돌아옴
    res = max(res, go[x] + back[i])

print(res)