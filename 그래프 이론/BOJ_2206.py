# 벽 뿌수고 이동하기, G3, BFS

from sys import stdin
from collections import deque

# 벽을 한개까지만 부술 수 있음
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))
# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a, b, c):
    q = deque()
    q.append([a, b, c])

    while q:
        x, y, z = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and z == 0:   # 벽 파괴 가능, 다음 움직임이 벽임
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])

                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])


    return -1

print(bfs(0,0,0))
