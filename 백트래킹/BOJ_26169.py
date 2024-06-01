# 세번 이내에 사과를 먹자, S3
from sys import stdin

graph = [[] for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
for i in range(5):
    graph[i] = list(map(int, stdin.readline().split()))

r, c = map(int, stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def dfs(depth, x, y, cnt):
    visited[x][y] = 1
    
    if cnt >= 2:
        return 1

    if depth > 2:
        visited[x][y] = 0
        return 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and graph[nx][ny] != -1:
            if graph[nx][ny] == 1:
                if dfs(depth + 1, nx, ny, cnt + 1) == 1:
                    return 1
            else:
                if dfs(depth + 1, nx, ny, cnt) == 1:
                    return 1

    visited[x][y] = 0
    return 0

print(dfs(0, r, c, 0))