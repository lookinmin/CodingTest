# 주사위 굴리기, G4, 구현-시뮬레이션
# 사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

from sys import stdin

n, m , x, y, k = map(int, stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

move = list(map(int, stdin.readline().split()))

dice = {
    1 : 0,          # 초기 위
    2 : 0,          # 앞
    3 : 0,          # 오른쪽
    4 : 0,          # 왼쪽
    5 : 0,          # 뒤
    6 : 0           # 아래
}

if board[x][y]== 0:
    board[x][y] = dice[6]
else:
    dice[6] = board[x][y]
    board[x][y] = 0

for num in move:
    if num == 1:
        nx = x
        ny = y + 1
        if 0<=nx<n and 0<=ny<m:

            dice[3] = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            if board[nx][ny] == 0:
                board[nx][ny] = dice[6]
            else:
                dice[6] = board[nx][ny]
                board[nx][ny] = 0

            print(dice[1])
        x = nx
        y = ny
    elif num == 2:
        nx = x
        ny = y - 1
        if 0 <= nx < n and 0 <= ny < m:
            dice[4] = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            if board[nx][ny] == 0:
                board[nx][ny] = dice[6]
            else:
                dice[6] = board[nx][ny]
                board[nx][ny] = 0

            print(dice[1])
        x = nx
        y = ny
    elif num == 3:
        nx = x - 1
        ny = y
        if 0 <= nx < n and 0 <= ny < m:
            dice[2] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            if board[nx][ny] == 0:
                board[nx][ny] = dice[6]
            else:
                dice[6] = board[nx][ny]
                board[nx][ny] = 0

            print(dice[1])
        x = nx
        y = ny
    else:
        nx = x + 1
        ny = y
        if 0 <= nx < n and 0 <= ny < m:
            dice[5] = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            if board[nx][ny] == 0:
                board[nx][ny] = dice[6]
            else:
                dice[6] = board[nx][ny]
                board[nx][ny] = 0

            print(dice[1])
        x = nx
        y = ny


import sys
input = sys.stdin.readline

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0] * 6

### 문제 이해하는 시간이 오래 걸렸다
### 주사위를 집어 올린다고 생각했다 처음엔
## 하지만! 방향에 따라 굴린다!
### 주사위를 굴리고난 후 숫자를 변경해줌.
for d in command:
    nx = x + dr[d]
    ny = y + dc[d]

    if not 0 <= nx < n or not 0 <= ny < m:      ## 범위 밖에 있는 좌표면 continue
        continue

    ## 헷갈리기 때문에 방향으로 명시해줌
    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    ### 방향에 따라 주사위 굴리기~~~!!
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif d == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif d == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    ## 지도에 숫자가 0일 때
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    ## 지도의 숫자가 0이 아닐 때
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    ## 꼭 값을 갱신해주기!
    x, y = nx, ny
    print(dice[4])