# 영역 구하기, S1, 그래프
# bfs

from sys import stdin
from collections import deque

m,n,k = map(int,stdin.readline().split())
graph = [[0] * n for _ in range(m)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append([x,y])
    cnt = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx,ny])
                cnt += 1
    return cnt

res = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))

print(len(res))
print(*sorted(res))