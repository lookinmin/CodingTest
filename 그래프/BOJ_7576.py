# 토마토, G5, 그래프-BFS

from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

# 1 = 익음, 0 = 안익음, -1 = 토마토 없음
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])         # 여기서 따로 해주는 이유는, 이미 익은 토마토의 좌표를 q에 저장해주기 위해서

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        a, b = q.popleft()          # 현재 익은 토마토들에 대해 bfs 수행
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1         # 총 며칠 걸리는 지 확인하기 위해 +1씩 해주며 증가
                q.append([nx, ny])


bfs()
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)        # 1부터 시작했으니까 -1
