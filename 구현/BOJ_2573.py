# 빙산, G4, 구현 - 그래프

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    sea = []

    while q:
        a, b = q.popleft()
        s = 0               # 주위를 감싸는 바다의 수
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    s += 1      # 바다의 수 증가
                elif graph[nx][ny] != 0 and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        if s > 0:
            sea.append((a, b, s))       # 바다의 위치를 리스트에 추가
    for a,b,s in sea:                   # 빙산에서 주변 바다의 수 값만큼 빼준다
        graph[a][b] = max(0, graph[a][b] - s)

    return 1

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

ice = []

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice.append((i,j))

year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    tmp = []            # 녹은 빙산의 위치를 저장할 배열
    group = 0

    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)              # 빙산이 있는 위치만큼 bfs()를 돔
        if graph[i][j] == 0:                # bfs()종료 후, 물이 된 부분 확인
            tmp.append((i,j))

    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(tmp)))     # 다 녹은 빙산은 탐색할 필요가 없으므로 ice에서 제거
    year += 1

if group < 2:
    print(0)



