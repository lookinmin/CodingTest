# 죽음의 게임, S3
from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = dict()
for i in range(n):
    pick = int(stdin.readline().rstrip())
    graph[i] = pick

visited = [0] * n

def bfs():
    q = deque()
    q.append(0)
    visited[0] = 1

    while q:
        now = q.popleft()
        if now == k:
            break

        nxt = graph[now]

        if not visited[nxt]:
            visited[nxt] = visited[now] + 1
            q.append(nxt)

bfs()
print(visited[k] - 1)

