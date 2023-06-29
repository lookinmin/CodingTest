# 양, S1, BFS
from sys import stdin
from collections import deque


r, c = map(int, stdin.readline().split())

graph = [[] for _ in range(r)]
dx = [-1 , 1, 0 ,0]
dy = [0, 0,-1,1]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    graph[i] = list(stdin.readline().rstrip())

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    sheep = 0
    wolf = 0

    if graph[x][y] == 'v':
        wolf += 1
    elif graph[x][y] == 'o':
        sheep += 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '#' and visited[nx][ny] == 0:
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                visited[nx][ny] = 1
                q.append([nx,ny])

    return sheep, wolf

arr = []
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and visited[i][j] == 0:
            arr.append(bfs(i, j))

S = 0
W = 0
for tmp in arr:
    if tmp[0] > tmp[1]:
        S += tmp[0]
    else:
        W += tmp[1]

print(S, W)