from sys import stdin
from collections import deque
# 1이 벽
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

must = []
for i in range(m):
    a, b = map(int, stdin.readline().split())
    must.append([a - 1, b - 1])

# start = must[0]
# end = must[-1]
route = []
def dfs(tmp, depth):
    if depth == m:
        route.append(tmp)
        return

    if tmp[-1] == must[depth]:        # 현재 방문지점이 must의 현 순서이다.
        dfs(tmp, depth + 1)           # 방문처리하고 ㄱ

    x = tmp[-1][0]
    y = tmp[-1][1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            if [nx, ny] not in tmp:          # 이번 경로에 방문하지 않았음
                dfs(tmp + [[nx, ny]], depth) # must에 있는진 이후에 확인하고 일단 ㄱ

dfs([must[0]], 0)
print(len(route))