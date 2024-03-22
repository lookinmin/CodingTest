# 로봇, S2
from sys import stdin

r, c = map(int, stdin.readline().split())
board = [[0] * c for _ in range(r)]
k = int(stdin.readline())
for _ in range(k):
    kr, kc = map(int, stdin.readline().split())
    board[kr][kc] = 1

x, y = map(int, stdin.readline().split())
board[x][y] = 1
direction = list(map(int, stdin.readline().split()))

dx = [-1, 1, 0, 0]      # 상하좌우
dy = [0, 0, -1, 1]

pos = 0
dirSet = set()

res = []

while 1:
    dirSet.add(direction[pos])
    nx = x + dx[direction[pos] - 1]
    ny = y + dy[direction[pos] - 1]
    if 0<=nx<r and 0<=ny<c and board[nx][ny] == 0:
        dirSet = set()
        board[nx][ny] = 1
        x = nx
        y = ny
    else:
        pos = (pos + 1) % 4     # 다음 방향
        if direction[pos] in dirSet:
            # 이미 간 방향
            res = [x, y]
            break
        else:
            continue

print(*res)