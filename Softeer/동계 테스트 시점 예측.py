from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 0,0 부터 시작해서 각 지점이 얼음에 2번 이상 닿는지 확인

def bfs(a, b, temp):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    temp[nx][ny] += 1
    return temp
                
                    
cnt = 0               
while 1 in (num for row in graph for num in row):
    cnt += 1
    visited = [[0] * m for _ in range(n)]
    temp = [[0] * m for _ in range(n)]
    bfs(0, 0, temp)
    
    for x in range(n):
        for y in range(m):
            if temp[x][y] >= 2:
                graph[x][y] = 0
print(cnt)