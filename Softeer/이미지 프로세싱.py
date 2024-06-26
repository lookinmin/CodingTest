from sys import stdin
from collections import deque
import copy

h, w = map(int, stdin.readline().split())
graph = [[] for _ in range(h)]

for i in range(h):
    graph[i] = list(map(int, stdin.readline().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a, b, value):
    tmp = copy.deepcopy(graph)
    
    con = graph[a][b]
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    tmp[a][b] = value

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and graph[nx][ny] == con:
                tmp[nx][ny] = value
                visited[nx][ny] = 1
                q.append([nx, ny])
    return tmp

q = int(stdin.readline())
for _ in range(q):
    visited = [[0] * w for _ in range(h)]
    i, j, c = map(int,stdin.readline().split())
    i = i - 1
    j = j - 1
    graph = bfs(i, j, c)

for i in range(h):
    print(*graph[i])