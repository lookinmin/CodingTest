# 두 동전, G4, BFS-백트래킹

from sys import stdin
from collections import deque
# 벽이면 이동 안하고 밖이면 떨어짐
# 그래프에서 움직이는 대상이 2개인 경우 어떻게 해야될까
n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

sx = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            sx.append([i, j])
q.append((sx[0][0], sx[0][1], sx[1][0], sx[1][1], 0))       # 0은 버튼 클릭 수


def bfs():
    while q:
        x, y, cx, cy, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx = x + dx[i]
            ncx = cx + dx[i]
            ny = y + dy[i]
            ncy = cy + dy[i]

            if 0<= nx <n and 0<=ny<m and 0<=ncx<n and 0<=ncy<m:
                if graph[nx][ny] == '#':
                    nx, ny = x, y
                if graph[ncx][ncy] == '#':
                    ncx, ncy = cx, cy
                q.append((nx,ny,ncx,ncy,cnt + 1))
            elif 0<=nx<n and 0<=ny<m:
                # cx 코인 떨어짐
                return cnt + 1
            elif 0<=ncx<n and 0<=ncy<m:
                return cnt + 1
            else:
                continue
    return -1

tmp = bfs()
print(tmp)