# 소문난 칠공주, G3, BFS
from sys import stdin
from collections import deque

graph = [[] for _ in range(5)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(5):
    graph[i] = list(map(str, stdin.readline().rstrip()))

res = 0

route = []

def bfs(route):
    visited = [[1] * 5 for _ in range(5)]
    q = deque()

    for x, y in route:
        visited[x][y] = 0
    sx, sy = route[0][0], route[0][1]
    visited[sx][sy] = 1

    q.append([sx, sy])
    check = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny] = 1
                check += 1
                q.append([nx, ny])

    if check != 7:
        return False
    else:
        return True

def dfs(depth, start, cnt):
    global res
    if cnt >= 4:        # 'Y'가 4개 이상 -> 실패
        return

    if depth == 7:
        if bfs(route):
            res += 1
        return

    for i in range(start, 25):
        r = i // 5
        c = i % 5

        route.append((r,c))
        dfs(depth + 1, i + 1, cnt + (graph[r][c] == 'Y'))
        route.pop()

dfs(0, 0, 0)
print(res)