import heapq
from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())
# n = 노드 수, m = edge 수
start = int(stdin.readline())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
# heapq를 사용할 때는 최단거리를 고르는 함수와 visited가 필요 없음


for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))       # 시작 노드로 가기위한 최단 경로는 0
    dist[s] = 0

    while q:
        distance, now = heapq.heappop(q)
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        if dist[now] < distance:        # 현재 노드가 이미 처리됬다면
            continue                    # 무시하고 진행

        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:       # 현재 노드를 거쳐가는게 더 짧음
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])