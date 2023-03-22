# 지름길, S1, 다익스트라

from sys import stdin
import heapq

n, d = map(int, stdin.readline().split())
# n = 지름길의 개수 , d = 고속도로의 길이
graph = [[] for _ in range(d+1)]
# 0~d까지의 1단위 길이를 모두 노드로

for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    start, end, length = map(int, stdin.readline().split())
    if end > d:
        continue
    graph[start].append((end, length))


# 다익스트라 문제풀이

INF = 987654321
dist = [INF] * (d+1)
dist[0] = 0

q = []
heapq.heappush(q, (0,0))
while q:
    k, now = heapq.heappop(q)
    if dist[now] < k:
        continue

    for x in graph[now]:
        cost = k + x[1]
        if dist[x[0]] > cost:
            dist[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))
print(dist[d])