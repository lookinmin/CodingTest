# 파이프 옮기기, G5, 그래프

from sys import stdin
import sys
sys.setrecursionlimit(10**9)

n = int(stdin.readline())
graph = [[0]* n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

cnt = 0

def dfs(x,y,z):
    global cnt

    if x == n-1 and y == n-1:
        cnt += 1
        return

    if x+1<n and y+1<n:
        if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
            dfs(x+1, y+1, 2)        # 대각선으로 이동했음 -> 2

    if z == 0 or z == 2:
        if y + 1 < n and graph[x][y+1] == 0:
                dfs(x,y+1,0)        # 가로로 이동했음 -> 0

    if z == 1 or z == 2:
        if x + 1<n and graph[x+1][y] == 0:
            dfs(x+1,y,1)

dfs(0,1,0)

print(cnt)