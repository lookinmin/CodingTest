from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [stdin.readline().strip() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_points, is_human):
    q = deque()
    visited = [[-1] * m for _ in range(n)]

    for (x, y) in start_points:
        q.append((x, y, 0))
        visited[x][y] = 0

    while q:
        x, y, cnt = q.popleft()

        if is_human and graph[x][y] == 'D':
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if is_human:
                    if graph[nx][ny] != '#':
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = cnt + 1
                else:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt + 1

    return visited if not is_human else -1

namwoo_start = []
ghost_start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'N':
            namwoo_start.append((i, j))
        elif graph[i][j] == 'G':
            ghost_start.append((i, j))

ghost_times = bfs(ghost_start, False)

namwoo_time = bfs(namwoo_start, True)

if namwoo_time != -1:
    can_escape = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'D' and ghost_times[i][j] != -1 and ghost_times[i][j] <= namwoo_time:
                can_escape = False
                break
        if not can_escape:
            break
    if can_escape:
        print("Yes")
    else:
        print("No")
else:
    print("No")
