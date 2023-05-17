# 오델로, S1, 구현

from sys import stdin

# 시작은 검은돌부터
n = int(stdin.readline())
board = [['.']*7 for _ in range(7)]

board[3][3], board[4][4] = 'W','W'
board[3][4], board[4][3] = 'B','B'

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def check(r, c, i, d):
    nx, ny = r, c
    visited[nx][ny] = 1
    if i%2 == 0:        # 흑
        while 1:
            nx += dx[d]
            ny += dy[d]

            if nx < 1 or nx > 6 or ny < 1 or ny > 6:
                break
            if visited[nx][ny] == 1 or board[nx][ny] == '.':        # 이미 방문, 빈칸임
                break
            # 탐색 위치에 흑돌이 있으면 양쪽 포위에 이미 돌 위치
            if board[nx][ny] == 'B':
                return 1
            visited[nx][ny] = 1
    else:
        while 1:
            nx += dx[d]
            ny += dy[d]
            if nx < 1 or nx > 6 or ny < 1 or ny > 6:
                break
            if visited[nx][ny] == 1 or board[nx][ny] == '.':        # 이미 방문, 빈칸임
                break
            if board[nx][ny] =='W':
                return 1
            visited[nx][ny] = 1
    return 0

def color(i):
    for j in range(1, 7):
        for k in range(1, 7):
            if i % 2 == 0 and visited[j][k] == 1:
                board[j][k] = 'B'       # 흑돌일때 방문 -> 흑돌로 뒤집기
            elif i % 2 == 1 and visited[j][k] == 1:
                board[j][k] = 'W'       # 백돌로 방문 -> 백돌로 뒤집기


for i in range(n):
    r, c = map(int, stdin.readline().split())
    for d in range(8):  # 8방향 탐색
        visited = [[0] * 7 for _ in range(7)]
        if check(r, c, i, d):
            color(i)

w, b= 0, 0
for i in range(1, 7):
    for j in range(1, 7):
        if board[i][j] == 'B':
            b += 1
        elif board[i][j] == 'W':
            w += 1
        print(board[i][j], end="")
    print()

if b > w:
    print("Black")
else:
    print("White")
