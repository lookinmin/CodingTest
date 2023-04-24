# 노드사이의 거리, G5, Tree

from sys import stdin
from collections import deque

n ,m = map(int, stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(start, goal):
    visited = [0] * (n+1)
    q = deque()
    q.append((start, 0))        # 시작점에서 edge의 weight는 0
    visited[start] = 1

    while q:
        v, w = q.popleft()      # 노드와 weight를 pop
        if v == goal:           # pop한 노드가 도착점이라면 거리 리턴
            return w
        for i, l in graph[v]:       # 해당 노드와 인접한 노드의 노드 번호(i), 간선의 weight(l)
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, w + l))        # weight 합산

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(bfs(a,b))
