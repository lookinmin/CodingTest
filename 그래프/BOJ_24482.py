# 알고리즘 수업 - 깊이 우선 탐색 4, S2
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

n, m, start = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    graph[v].sort(reverse= True)
    for node in graph[v]:
        if visited[node] == -1:
            visited[node] = visited[v] + 1
            dfs(node)

visited[start] = 0
dfs(start)

for v in visited[1:]:
    print(v)
