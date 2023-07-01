# 비밀 모임, G4, 다익스트라

from sys import stdin
import heapq
INF = int(1e9)
t = int(stdin.readline())

def dijkstra(s, graph, dist):
    q = []
    heapq.heappush(q, (0, s))       # 값, 노드
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


for _ in range(t):
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n+1)]


    for i in range(m):
        a, b, c = map(int, stdin.readline().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    k = int(stdin.readline())
    nowRooms = list(map(int, stdin.readline().split()))

    res = [0] * (n+1)        # 각 사람마다의 거리의 누적치
    for i in nowRooms:
        dist = [INF] * (n + 1)      # 사람마다 거리 초기화
        dijkstra(i, graph, dist)
        for j in range(1, n+1):
            res[j] += dist[j]
    minn = 0
    noww = INF
    for i in range(1, n + 1):
        if noww > res[i]:
            noww = res[i]
            minn = i
    print(minn)

