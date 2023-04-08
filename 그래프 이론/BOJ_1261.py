# 알고스팟, G4, 그래프 탐색-bfs

from sys import stdin
from collections import deque
import heapq

m,n = map(int, stdin.readline().split())
graph=[[]for _ in range(n)]
dist = [[-1]*m for _ in range(n)]       # 벽 부순 횟수 저장
for i in range(n):
    graph[i] = list(map(int,stdin.readline().rstrip()))


def bfs(x,y):

    q = deque()
    q.append((x,y))
    dist[0][0] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        a, b = q.popleft()          # 벽이 없는 곳을 우선적으로 방문
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if dist[nx][ny] == -1:      # 해당 방 방문 안함
                    if graph[nx][ny] == 0:
                        dist[nx][ny] = dist[a][b]
                        q.appendleft((nx,ny))       # 여기가 중요!   -> 벽이 없는 곳을 우선적으로 방문할 것
                        # 0인 방과 1인 방을 appendleft와 append로 구분
                    else:
                        dist[nx][ny] = dist[a][b] + 1
                        q.append((nx,ny))

bfs(0,0)
print(dist[n-1][m-1])

