# 최소비용 구하기, G5, 다익스트라
# 도시 = 노드 = n개
# 버스 = edge = m개

from sys import stdin
import heapq

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))

start, end = map(int, stdin.readline().split())

def dijkstra(s):                    # 다익스트라 짜는 법 외워라 민수야
    q = []
    heapq.heappush(q, (0,s))        # 비용, 현재 노드
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)

        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(dist[end])