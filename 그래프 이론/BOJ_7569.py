# 토마토, G5, 그래프-BFS

from sys import stdin
from collections import deque
# 상하좌우 + 위 아래

m, n, h = map(int ,stdin.readline().split())
# h = 쌓아올리는 상자의 수

graph = [[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, stdin.readline().split()))


q = deque()
def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        z,x,y = q.popleft()     # 높이, x, y
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1      # 몇일 걸리는 지 알아야되니까 더하기
                    q.append((nz,nx,ny))                        # 3차원 그래프는 z,x,y 순으로 삽입

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:             # 익은 토마토들을 전부 q에 넣고
                q.append((i,j,k))

bfs() # bfs() 시작

flag = 0
res = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:     # 안익은 토마토가 있다?
                flag = 1
            res = max(res, graph[i][j][k])          # 몇일걸렸는지 확인, 만약에 -1이면 시작부터 전부 익어있는거임

if flag == 1:       # 토마토가 익을수 없는 경우
    print(-1)
elif res == -1:     # 시작부터 전부 익어있는 경우
    print(0)
else:
    print(res - 1)  # 마지막 하루 빼줌
