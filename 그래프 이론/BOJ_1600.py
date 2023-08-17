# 말이 되고픈 원숭이, G3, BFS

from sys import stdin
from collections import deque

# k번만 나이트 처럼 이동 가능
k = int(stdin.readline())
w, h = map(int, stdin.readline().split())
graph = [[] for _ in range(h)]


for i in range(h):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
kx = [-2, -1, 1, 2, 2, 1, -1, -2]
ky = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(a, b, k):
    visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((a,b,k))     # k만큼 움직일 수 있는 횟수, 이동횟수
    visited[a][b][k] = 1

    while q:
        x, y, k = q.popleft()

        if x == h-1 and y == w - 1:
            return visited[h-1][w-1][k] - 1
        if k > 0:
            for i in range(8):
                nx = x + kx[i]
                ny = y + ky[i]

                if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 0 and visited[nx][ny][k-1] == 0:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    q.append((nx,ny,k-1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 0 and visited[nx][ny][k] == 0:
                visited[nx][ny][k] = visited[x][y][k] + 1
                q.append((nx,ny,k))
    return -1

print(bfs(0,0, k))
