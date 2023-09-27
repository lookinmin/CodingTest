# 미로 탐색, S1, 그래프 - BFS
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1 ,1]
# 상 하 좌 우

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:      #벽
                continue
            if nx == 0 and ny == 0:     # 처음으로 돌아간 경우
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))