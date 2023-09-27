# 중량제한, G3, 그래프

from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(1, n + 1):
        graph[i].sort(reverse=True, key= lambda x : x[1])

start, final = map(int, stdin.readline().split())

# 가는 경로 중 edge의 최솟값 찾기

res = int(1e9)

weight = [0]*(n+1)
def bfs(s, e):
    q = []
    heapq.heappush(q,(0, s))

    while q:
        distance, now = heapq.heappop(q)
        distance = -1 * distance        # 최대힙을 이용해야 됨 why? 두 노드를 연결하는 다리가 여러개 일 수 있어서

        if now == e:
            print(distance)
            break

        if weight[now] > distance:        # < 가 아닌 > => 최대 중량을 찾는거기 때문에
            continue

        for v, w in graph[now]:     # reversed 정렬을 통해 무게가 무거운거 부터 나옴
            if distance == 0:
                weight[v] = w
                heapq.heappush(q, (-1 * weight[v], v))
            elif weight[v] < w and weight[v] < distance:
                weight[v] = min(distance, w)        # 이전도시까지의 최대 중량, 현재 다리의 최대 중량 중 더 작은거
                heapq.heappush(q, (-1 * weight[v], v))

bfs(start, final)
