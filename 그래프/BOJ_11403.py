# 경로 찾기, S1, 그래프
# 인접 행렬 풀이

from collections import deque
from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(v):
    q = deque()
    q.append(v)
    check = [0 for _ in range(n)]       # 간선에 해당 정점이 연결되어있는지 기록

    while q:
        x = q.popleft()
        for i in range(n):
            if check[i] == 0 and graph[x][i] == 1:      # 연결되어있으면 방문
                q.append(i)
                check[i] = 1
                visited[v][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)

