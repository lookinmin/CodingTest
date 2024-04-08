# 호석이 두 마리 치킨, G5
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[0] * n for _ in range(n)]
x, y = map(int, stdin.readline().split())
x -= 1
y -= 1

endPoint = []
for i in range(m):
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1
    endPoint.append([a, b])

res = []

def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1

    dx,dy = [-1,-2,-2,-1,1,2,2,1], [-2,-1,1,2,-2,-1,1,2]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1


visited = [[0] * n for _ in range(n)]
bfs(x, y)

for x, y in endPoint:
    res.append(visited[x][y] - 1)

print(*res)