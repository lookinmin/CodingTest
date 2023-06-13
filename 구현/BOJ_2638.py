# 치즈, G3, 구현-bfs

from sys import stdin
from collections import deque
# 내부는 녹지 않음 -> 외부에서부터 BFS

n,m = map(int, stdin.readline().split())

graph = [[0] * m for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

res = 0

while 1:
    q = deque()
    visited = [[0] * m for _ in range(n)]

    visited[0][0] = 1
    q.append([0,0])     # 0,0부터 -> 외부부터

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]:       # 치즈임
                    graph[nx][ny] += 1  # 닿아있는 면 하나당 + 1
                else:                   # 공기임
                    visited[nx][ny] = 1 # 공기 방문 처리
                    q.append([nx, ny])

    flag = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:        # 2면이상 닿아있음
                graph[i][j] = 0
            elif graph[i][j] > 0:
                flag = 1                # 치즈가 하나라도 남아있음
                graph[i][j] = 1         # 한면 닿아있던거 초기화
    res += 1

    if flag == 0:
        print(res)
        break
