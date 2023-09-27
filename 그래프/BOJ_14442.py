# 벽 부수고 이동하기2, G3, BFS

from sys import stdin
from collections import deque

# 벽을 k개까지 부실 수 있음

n, m, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]


def bfs(a, b, c):
    q = deque()
    q.append([a,b,c])
    visited[a][b][c] = 1

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx,ny,z])
                elif graph[nx][ny] == 1 and z > 0 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    q.append([nx, ny, z-1])

    return -1

print(bfs(0,0,k))

# 2206 번과 비슷하지만
# 2206은 1개만 부실 수 있어 k를 0, 1로 만들면 되지만
# k개 유동적이므로 k개에서 -1씩해서 >0 까지 가는게 중요하다
