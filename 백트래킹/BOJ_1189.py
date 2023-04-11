# 컴백홈, S1, 백트래킹

from sys import stdin
r,c,K = map(int, stdin.readline().split())

graph = [['.'] * c for _ in range(r)]
for i in range(r):
    graph[i] = list(map(str,stdin.readline().rstrip()))

res = 0

def dfs(x,y,k):
    global res

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if k == K:
        if (x,y) == (0, c-1):
            res += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] != 'T':
                graph[nx][ny] = 'T'         # 한번 간 곳은 못가게
                dfs(nx,ny,k+1)              # dfs를 수행한 후
                graph[nx][ny] = '.'         # 바꿔줘야 함

graph[r-1][0] = 'T'
dfs(r-1, 0, 1)
print(res)
