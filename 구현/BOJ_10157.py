# 자리 배정, 실버4, 구현-브루트포스, 다시

from sys import stdin
c, r = map(int, stdin.readline().split())
k = int(stdin.readline())
# c = 가로, r = 세로
if k > c*r:
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 서 남 동 북

grid = [[0]*c for _ in range(r)]
direction = x = y = 0
for seat in range(1, c*r+1):
    if seat == k:
        print(y+1,x+1)
        break
    else:
        grid[x][y] = seat
        x += dx[direction]
        y += dy[direction]

        if x <0 or y<0 or x >= r or y >= c or grid[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction+1) % 4
            x += dx[direction]
            y += dy[direction]