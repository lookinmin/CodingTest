# 선수과목, G5, 위상정렬

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
res = [1] * (n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    inDegree[b] += 1

def topo():
    q = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for v in graph[now]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                res[v] = res[now] + 1
                q.append(v)

topo()
print(*res[1:])

