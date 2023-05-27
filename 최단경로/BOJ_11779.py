# 최소비용 구하기2, G3, 다익스트라

from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

prev_node = [0] * (n+1)     # 경로 저장 리스트

for i in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((b,c))

start, end = map(int, stdin.readline().split())

def dikjstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue

        for v, w in graph[now]:
            cost = w + distance
            if cost < dist[v]:
                dist[v] = cost
                prev_node[v] = now          # 인접한 노드에 대한 이전 방문은 현재 위치한 노드임
                heapq.heappush(q, (cost, v))

dikjstra(start)

print(dist[end])

path = [end]        # 거꾸로 거슬러 올라가기
here = end
while here != start:
    here = prev_node[here]
    path.append(here)

path.reverse()
print(len(path))
print(*path)