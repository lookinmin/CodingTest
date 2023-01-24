# 바이러스, S3, 그래프 이론 - connected component 수 찾기
from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
graph=[[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

# for i in range(n):
#     print(*graph[i])

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

bfs(1)

print(sum(visited) - 1 )