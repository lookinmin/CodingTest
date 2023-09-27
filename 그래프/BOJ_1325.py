# 효율적인 해킹, S1, 그래프
# 인접 리스트 방식
# bfs
# directed graph

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,stdin.readline().split())
    graph[b] += [a]


def bfs(v):
    visited = [0] * (n+1)
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt

res = []
maxCnt = 1

for i in range(1, n+1):
    tmp = bfs(i)
    if tmp > maxCnt:
        maxCnt = tmp
        res.clear()
        res.append(i)
    elif tmp == maxCnt:
        res.append(i)

print(*res)