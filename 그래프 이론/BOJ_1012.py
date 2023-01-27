# 유기농 배추, S2, 그래프 이론-탐색
# connected component

from sys import stdin
from collections import deque

# 그래프 선언을 2차원 배열로 해서, 1로 만들어 탐색하는 경우와
# graph[a] += [b]로 선언하여 푸는 경우를 구분하여 학습해야함

T = int(stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, graph):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    return


for _ in range(T):
    cnt = 0
    n, m, k = map(int, stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, graph)
                cnt += 1
    print(cnt)