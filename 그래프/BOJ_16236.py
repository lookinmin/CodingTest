# 아기 상어, G3, 그래프

from sys import stdin
from collections import deque

shark = 2

n = int(stdin.readline())
graph = [[] for _ in range(n)]


for i in range(n):
    graph[i] = list(map(int,stdin.readline().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

pos = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0

def bfs(x,y):
    visited = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    tmp = []            # 먹이 위치들의 좌표 저장 리스트

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if graph[nx][ny] !=0 and graph[x][y] > graph[nx][ny]:
                    visited[nx][ny] = visited[a][b] + 1
                    tmp.append((visited[nx][ny]-1, nx, ny))
                elif graph[x][y] == graph[nx][ny]:      # 왜(x,y)랑 비교하는거지 a,b가 아니라
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx,ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx,ny))

    return sorted(tmp, key= lambda x: (x[0], x[1], x[2]))

x, y = pos
size = [2,0]        # 시작 크기는 2, 먹이 먹는건 0개부터

while 1:
    graph[x][y] = size[0]
    tmp = deque(bfs(x,y))

    if not tmp:         # tmp 내부의 값을 전부 꺼냈으면
        break

    step, nx, ny = tmp.popleft()
    cnt += step

    size[1] += 1

    if size[0] == size[1]:      # 크기 만큼 먹이 먹었으면,
        size[0] += 1
        size[1] = 0

    graph[x][y] = 0
    x,y = nx,ny

print(cnt)









