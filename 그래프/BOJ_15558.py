# 점프 게임, G5
from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
left = list(map(int, stdin.readline().rstrip()))
right = list(map(int, stdin.readline().rstrip()))

visitedLeft = [0] * (n + 1)     # True
visitedRight = [0] * (n + 1)    # False
graph = [left, right]
visited = [visitedLeft, visitedRight]
visited[0][0] = 1
dx = [1, -1, k]

def bfs():
    idx = 0
    q = deque()
    q.append((idx, 0, 0))
    while q:
        now, pos, time = q.popleft()

        for i in range(3):
            nx = now + dx[i]

            if nx >= n:
                return 1

            if i < 2:
                if time < nx and graph[pos][nx] == 1:
                    if not visited[pos][nx]:
                        visited[pos][nx] = 1
                        q.append((nx, pos, time + 1))

            else:
                if time < nx and graph[1 - pos][nx] == 1:
                    if not visited[1 - pos][nx]:
                        visited[1 - pos][nx] = 1
                        q.append((nx, 1-pos,time + 1))

    return 0

print(bfs())