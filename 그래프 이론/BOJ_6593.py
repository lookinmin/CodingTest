# 상범 빌딩, G5, BFS
# 3차원 BFS

from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]        # 상하좌우위아래

def bfs(a, b, c):
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = 1

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<L and 0<=ny<R and 0<=nz<C:
                if graph[nx][ny][nz] == 'E':
                    print("Escaped in {} minute(s).".format(visited[x][y][z]))
                    return
                if graph[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx,ny,nz))
    print("Trapped!")

while 1:
    L, R, C = map(int ,stdin.readline().split())
    if L == R == C == 0:
        break

    graph = [[[] for _ in range(R)] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]


    for i in range(L):
        graph[i] = [list(map(str, stdin.readline().rstrip())) for _ in range(R)]
        stdin.readline()

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    bfs(i, j, k)