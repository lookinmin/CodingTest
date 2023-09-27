# 적록 색약, G5, 그래프

from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [list(stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0 ,0 ,-1 , 1]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[a][b] == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))

cnt1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1           # 분리된 공간 갯수 세주기

for i in range(n):              # 색약이니까 G->R로 바꿔줌
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]       # 초기화
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)
