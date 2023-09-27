# 너비 우선 탐색 1, S2, BFS
from sys import stdin
from collections import deque

n, m, r=map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u] += [v]
    graph[v] += [u]

cnt = 1
def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        c = q.popleft()
        graph[c].sort()                 # 오름차순 정렬을 해줘야 함
        for i in graph[c]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt        # 여기 중요
                q.append(i)

bfs(r)

for i in visited[1:]:
    print(i)