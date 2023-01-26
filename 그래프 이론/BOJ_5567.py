# 결혼식, S2, 그래프 이론, 그래프 탐색
# BFS

from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
graph =  [[] for _ in range(n+1)]
visited = [0] * (n + 1)

def bfs(v):
    visited[v] = 1
    q = deque([v])
    while q:
        c = q.popleft()
        for i in graph[c]:
            if visited[i] == 0:
                visited[i] = visited[c] + 1     # 방문 횟수를 세준다.
                q.append(i)


for i in range(m):
    a, b= map(int, stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

# 친구 & 친구의 친구

bfs(1)
print(visited.count(2) + visited.count(3))

