# 숨바꼭질, S1, 그래프-BFS

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
Max = 10**5
graph = [0] * (Max + 1)

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if x == K:
            return graph[x]
        for nx in (x-1, x+1, x * 2):                    # 이렇게도 for문 구성할 수 있다는걸 알아야함
            if 0<= nx <=Max and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)



print(bfs(N))
