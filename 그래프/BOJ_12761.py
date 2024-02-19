# 돌다리, S1

from sys import stdin
from collections import deque

A, B, N, M = map(int,stdin.readline().split())

visited = [0] * 100001

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    move = [-1, 1, -1 * A, -1 * B, A, B, A, B]

    while q:
        now = q.popleft()

        for i in range(8):
            if i < 6:
                nx = now + move[i]
                if 0<=nx<100001 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = visited[now] + 1

            elif i == 6 or i == 7:
                nx = now * move[i]
                if 0<=nx<100001 and not visited[nx]:
                    q.append(nx)
                    visited[nx] = visited[now] + 1

bfs(N)
print(visited[M] - 1)
