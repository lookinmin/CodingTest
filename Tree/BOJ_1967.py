# 트리의 지름, G4, 트리-DFS

from sys import stdin
import sys

sys.setrecursionlimit(10**9)
# 트리의 경로 중 가장 긴 것의 길이
# 노드간 절대적인 거리가 아니라 가중치의 합이 가장 큰 거 찾기
# 1. 아무 노드나 잡고 가장 먼 노드 구하기
# 2. 해당 노드에서 가장 먼 노드 한번 더 구하기

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dfs(s, weight):
    for v, w in graph[s]:
        if visited[v] == -1:
            visited[v] = weight + w
            dfs(v, weight + w)

visited = [-1]*(n+1)
visited[1] = 0      # 언제나 루트는 1

dfs(1, 0)       # 루트에서 가장 먼 노드를 찾는다

farnode = visited.index((max(visited)))     # 루트에서 가장 먼노드
visited = [-1]*(n+1)    # 초기화 (다시 찾아야되니까)
visited[farnode] = 0    # 이제 해당 노드를 루트로 삼아 다시 탐색
dfs(farnode, 0)

print(max(visited))