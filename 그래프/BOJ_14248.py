# 점프 점프, S2
from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = list(map(int, stdin.readline().split()))
start = int(stdin.readline())
visited = [0] * n

dx = [1, -1]
def bfs(start):
    q = deque()
    q.append(start)
    visited[start-1] = 1

    while q:
        now = q.popleft()

        for i in range(2):
            nx = now + (dx[i] * graph[now - 1])
            if 0 < nx <= n and not visited[nx - 1]:
                visited[nx - 1] = 1
                q.append(nx)

bfs(start)
cnt = 0
for i in range(n):
    if visited[i] != 0:
        cnt += 1

print(cnt)