from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []
def bfs(a, b):
    q = deque()
    q.append([a, b])
    cnt = 1
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                cnt += 1
                visited[nx][ny] = 1

    return cnt
                
        

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and not visited[x][y]:
            res.append(bfs(x, y))
print(len(res))
for val in sorted(res):
    print(val)