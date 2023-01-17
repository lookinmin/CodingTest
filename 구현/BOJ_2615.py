# 오목, 실버1, 구현-브루트포스(완탐)
import sys
input = sys.stdin.readline

board = []
for i in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            tmp = board[x][y]           # 1 or 2

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == tmp:        # 탐색중인게 바둑판 내부 이면서, 흑이거나 백이 유지될때
                    cnt += 1
                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x-dx[i]][y-dy[i]] == tmp:
                            break       # 육목 이상 ( 시작 돌 보다 좌측 기준 하나 더)
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == tmp:
                            break       # 육목 이상 ( 끝 돌보다 우측 기준 하나 더)
                        print(tmp)
                        print(x + 1, y + 1)
                        sys.exit(0)
                    nx += dx[i]
                    ny += dy[i]
print(0)
