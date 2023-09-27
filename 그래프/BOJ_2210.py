# 숫자판 점프, S2, 그래프
from sys import stdin

res = []
arr = [list(map(str, stdin.readline().split())) for _ in range(5)]

def dfs(x,y, num):
    if len(num) == 6:
        if num not in res:
            res.append(num)
        return

    dx = [-1,1,0,0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,num + arr[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j, arr[i][j])

print(len(res))