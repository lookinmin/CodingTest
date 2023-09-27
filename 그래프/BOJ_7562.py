# 나이트의 이동, S2, 그래프

from sys import stdin
from collections import deque
T = int(stdin.readline())

def bfs(a,b, ax, ay):
    q = deque()
    q.append([a,b])
    board[a][b] = 1
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    while q:
        x, y = q.popleft()
        if ax == x and ay == y:
            print(board[ax][ay] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny<l and board[nx][ny] == 0:
                q.append([nx, ny])
                board[nx][ny] = board[x][y] + 1     # 이동거리 구하기

for _ in range(T):
    l = int(stdin.readline())
    board = [[0]*l for _ in range(l)]
    nowx, nowy = map(int, stdin.readline().split())
    desx, desy = map(int, stdin.readline().split())
    if nowx == desx and nowy == desy:
        print(0)
    else:
        bfs(nowx, nowy, desx, desy)