# 구슬 찾기, G4

from sys import stdin

N, M = map(int, stdin.readline().split())
h_graph = [[] for _ in range(N + 1)]        # [노드] = [노드보다 무거운 것들]
l_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    # a > b
    h_graph[a].append(b)
    l_graph[b].append(a)

def dfs(graph, root):
    cnt = 0

    for v in graph[root]:
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            cnt += dfs(graph, v)

    return cnt

mid = (N+1) / 2
res = 0

for v in range(1, N + 1):
    visited = [0]*(N+1)

    if dfs(h_graph, v) >= mid:
        res += 1
    if dfs(l_graph, v) >= mid:
        res += 1

print(res)


