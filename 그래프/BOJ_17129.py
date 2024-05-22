# 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유, S1
from sys import stdin
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2 -> 3, 4, 5 중 가장 빠른 거 찾기

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

visited = [[0] * m for _ in range(n)]
res = int(1e9)

def bfs(sx, sy):
    global res
    q = deque()
    q.append([sx, sy, 0])
    visited[sx][sy] = 1
    
    while q:
        x, y, cnt = q.popleft()
        
        if graph[x][y] in [3, 4, 5]:
            res = min(res, cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny, cnt + 1])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

if res != int(1e9):
    print("TAK")
    print(res)
else:
    print("NIE")