# 촌수 계산, S2, 그래프 - bfs

from sys import stdin
from collections import deque

n = int(stdin.readline())

graph = [[] for _ in range(n+1)]

me, you = map(int, stdin.readline().split())
m = int(stdin.readline())

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        c = q.popleft()

        for i in graph[c]:
            if visited[i] == 0:
                visited[i] = visited[c] + 1
                q.append(i)


bfs(me)
if visited[you] == 0:
    print(-1)
else:
    print(visited[you])
