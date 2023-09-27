# 깊이 우선 탐색2, S2, DFS

from sys import stdin
import sys

sys.setrecursionlimit(10**9)

n, m, r = map(int ,stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n+1)
cnt = 1

def dfs(s):
    global cnt
    visited[s] = cnt

    for v in sorted(graph[s], reverse=True):
        if visited[v] == 0:
            cnt += 1
            dfs(v)

dfs(r)

for i in visited[1:]:
    print(i)