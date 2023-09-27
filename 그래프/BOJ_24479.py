# 깊이 우선 탐색, S2, DFS

import sys
sys.setrecursionlimit(10**9)                # dfs에서 런타임 에러 해결
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1
for _ in range(m):
    u, v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]

def dfs(v):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)

for i in visited[1:]:
    print(i)