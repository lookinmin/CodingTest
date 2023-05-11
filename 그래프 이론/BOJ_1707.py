# 이분 그래프, G4, 그래프

from sys import stdin
from collections import deque

K = int(stdin.readline())

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = -1 * visited[x]        # 다른 그룹으로 넣기
            elif visited[i] == visited[x]:
                return 0
    return 1

for _ in range(K):
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    res = 1
    for i in range(1, v+1):
        if visited[i] == 0:
            res = bfs(i)
            if res == 0:
                break

    if res == 1:
        print("YES")
    else:
        print("NO")
