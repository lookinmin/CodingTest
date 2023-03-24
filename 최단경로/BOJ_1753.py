# 최단경로, G4, 다익스트라

from sys import stdin
import heapq
# v가 20000개 까지 주어지므로 heapq

v, e = map(int, stdin.readline().split())
start = int(stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(v + 1)]
dist = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(s):
    q = []

    heapq.heappush(q, (0, s))                   # 큐에 넣을 떄는 (값, 노드)
    dist[s] = 0
    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue

        for i in graph[now]:
            cost = i[1] + distance
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))     # 갱신된 값, 노드번호 순으로 삽입

dijkstra(start)

for i in range(1, v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])