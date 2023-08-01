# 미세먼지 안녕!, G4, 구현

from sys import stdin
from collections import deque

r,c,t = map(int, stdin.readline().split())

room = [[] for _ in range(r)]

for i in range(r):
    room[i] = list(map(int, stdin.readline().split()))

up = -1
down = -1

for i in range(r):      # 공기 청정기 위치 확인
    if room[i][0] == -1:
        up = i
        down = i+1
        break

# 확산이 먼저

def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    tmp_arr = [[0]*c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if room[x][y] != 0 and room[x][y] != -1:
                tmp = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                        tmp_arr[nx][ny] += room[x][y] // 5
                        tmp += room[x][y] // 5
                room[x][y] -= tmp       # 몇번 빠지는 지

    for i in range(r):
        for j in range(c):
            room[i][j] += tmp_arr[i][j]



def air_up():
    dx = [0, -1, 0, 1]      # -> , ↑, <-, ↓
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0

    x, y = up, 1            # 공기청정기 바로 옆부터

    while 1:
        nx = x + dx[dir]    # 처음은 →
        ny = y + dy[dir]

        if x == up and y == 0:      # 공기정청기 닿으면 멈춤 (x, y) == (up, 0)
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:  # 끝에 닿으면
            dir += 1        # 방향 꺾음
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

def air_down():
    dx = [0, 1, 0, -1]       # →, ↓, ←, ↑
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0

    x, y = down, 1          # 공기청정기 바로 옆부터

    while 1:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

for _ in range(t):
    spread()
    air_up()
    air_down()
res = 0

for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            res += room[i][j]

print(res)