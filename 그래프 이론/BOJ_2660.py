# 회장 뽑기, G5, BFS

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

while 1:
    a, b = map(int, stdin.readline().split())
    if a==b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    q = deque([s])
    visited[s] = 0

    while q:
        x = q.popleft()
        for v in graph[x]:
            if visited[v] == -1:
                visited[v] = visited[x] + 1
                q.append(v)

num = 51
res = []
for i in range(1, n+1):
    visited=[-1]*(n+1)
    bfs(i)
    tmp = max(visited[1:])
    if tmp == num:
        res.append(i)
    elif tmp < num:
        res = [i]
        num = tmp

print(num, len(res))
print(*res)


