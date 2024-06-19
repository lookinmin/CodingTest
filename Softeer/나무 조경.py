from sys import stdin
n = int(stdin.readline())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]
res = 0

def dfs(x, y, depth, sum):
    global res, visited
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny] = 1
            tmp = sum + board[x][y] + board[nx][ny]
            if depth == 3 or (n < 3 and depth == 1):
                res = max(tmp, res)
                visited[nx][ny] = 0
                return

            for i in range(n):
                for j in range(n):
                    if not visited[i][j]:
                        dfs(i, j, depth + 1, tmp)
                        visited[i][j] = 0
            visited[nx][ny] = 0

for i in range(n):
    for j in range(n):
        dfs(i, j, 0, 0)
        visited[i][j] = 0

print(res)