# 스타트 링크, S1, 그래프

from sys import stdin
from collections import deque

F, S, G, U, D = map(int,stdin.readline().split())

# 건물의 총 수 = F / 목표지점 = G / 현재 = S

graph = [0 for _ in range(F+1)]
visited = [0 for _ in range(F+1)]

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == G:
            return graph[G]
        for i in (v+U, v-D): #U만큼 위로 or D만큼 아래로
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                graph[i] = graph[v] + 1
                q.append(i)

    if graph[G] == 0:
        return "use the stairs"



print(bfs(S))

