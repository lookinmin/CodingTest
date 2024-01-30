import sys
sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, px, py):
    if visited[x][y]:   # 방문했던 점을 다시 dfs로 탬색?
        print("Yes")    # cycle을 이룬다.
        exit()

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == color:
            if (nx, ny) != (px, py):        # 직전 탐색 위치는 탐색할 필요 없음
                dfs(nx, ny, color, x, y)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, graph[i][j], -1, -1)

print("No")