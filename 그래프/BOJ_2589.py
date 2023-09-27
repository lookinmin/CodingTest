# 보물섬, G5, 그래프

from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(stdin.readline().strip())

def bfs(x,y):
    q = deque()
    q.append((x,y))
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while q:
        a,b= q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[a][b] + 1     # 여기 잘 생각하기!
                cnt = max(cnt, visited[nx][ny])
                q.append((nx,ny))
    return cnt - 1

res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            res = max(res, bfs(i,j))

print(res)

