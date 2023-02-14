# 안전 영역, S1, 그래프-브루트포스
from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[0]*n for _ in range(n)]

max_num = 0
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))
    for j in graph[i]:
        if j > max_num:
            max_num = j

def bfs(x,y,limit):
    q = deque()
    q.append([x,y])
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    visited[x][y] = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > limit and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

res = []

for i in range(max_num):
    cnt = 0
    visited = [[0] * n for _ in range(n)]   # 각 물 높이마다 visited 초기화 해야함
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i)
                cnt += 1
    res.append(cnt)

print(max(res))