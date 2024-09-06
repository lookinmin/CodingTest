# S2, DFS
from sys import stdin
import sys
sys.setrecursionlimit(10**8)
n, m, s = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n + 1)
visited[s] = 0

def dfs(v):    
    for node in sorted(graph[v]):
        if visited[node] == -1:
            visited[node] = visited[v] + 1
            dfs(node)
    return

dfs(s)

for val in visited[1:]:
    print(val)