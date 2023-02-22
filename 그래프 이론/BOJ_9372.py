# 상근이의 여행, S4, 트리-그래프

from sys import stdin
from collections import deque

T = int(stdin.readline())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 0
    while q:
        q.popleft()
        for i in range(1, n+1):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt



for _ in range(T):
    n, m = map(int, stdin.readline().split())
    graph = [[0]*(m+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    val = 0
    for _ in range(m):
        a, b = map(int,stdin.readline().split())
        graph[a]+=[b]
        graph[b]+=[a]

    print(bfs(1))
