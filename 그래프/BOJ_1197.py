# G4, MST
from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def prim(start, graph):
    global v
    visited[start] = 1
    q = []
    for nxt_node, weight in graph[start]:
        heapq.heappush(q, (weight, nxt_node))
    
    total_weight = 0
    edge_count = 0  # v개의 정점을 연결하기 위한 최소한의 간선 수는 v - 1이다.
    
    while q and edge_count < v - 1:
        weight, node = heapq.heappop(q)
        
        if not visited[node]:
            visited[node] = 1
            total_weight += weight 
            edge_count += 1
            
            for nxt_node, nxt_weight in graph[node]:
                if not visited[nxt_node]:
                    heapq.heappush(q, (nxt_weight, nxt_node))
    return total_weight

print(prim(1, graph))