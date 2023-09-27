# 단지번호 붙이기, S1, 그래프

from sys import stdin
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    q = deque()
    q.append([x,y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    graph[x][y] = 0
    cnt = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])
                cnt += 1
    return cnt

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i,j))

res.sort()
print(len(res))
for i in res:
    print(i)

