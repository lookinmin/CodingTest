# ABCDE, G5, DFS
import sys
from sys import stdin
sys.setrecursionlimit(10**8)

# A-B-C-D-E

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [0] * 2001

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = False

def dfs(idx, depth):
    global res
    visited[idx] = 1

    if depth == 4:      # 친구관계가 4번 이상 연결
        res = True
        return

    for v in graph[idx]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v, depth + 1)
            visited[v] = 0

for i in range(n):          # 모든 친구관계 파악
    dfs(i, 0)
    visited[i] = 0
    if res:
        break

if res:
    print(1)
else:
    print(0)