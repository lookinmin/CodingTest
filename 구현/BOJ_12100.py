# 2048, G2, 구현

from sys import stdin
from copy import deepcopy

n = int(stdin.readline())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

res = 0

def move(board, dir):
    if dir == 0:        # 동쪽
        for i in range(n):
            top = n - 1     # 제일 동쪽부터
            for j in range(n-2, -1, -1):        # 서쪽으로 한칸씩 이동하면서
                if board[i][j]:
                    tmp = board[i][j]           # 현재값 저장
                    board[i][j] = 0             # 현재 위치 0으로 변경
                    if board[i][top] == 0:      # 가장 동쪽이 0 이라면
                        board[i][top] = tmp     # 값넣음
                    elif board[i][top] == tmp:  # 현재 값이랑 같다면
                        board[i][top] = tmp * 2 # 2배
                        top -= 1                # 마지노선을 하나 당김
                    else:
                        top -= 1                # 값이 있지만 나랑 다르다면
                        board[i][top] = tmp     # 마지노선 당기고, 마지노 선에다 내 값 할당

    if dir == 1:        # 서
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    if dir == 2:        # 남
        for j in range(n):
            top = n - 1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    if dir == 3:          # 북
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp
    return board

def back_tracking(board, cnt):
    global res
    if cnt == 5:        # 5번 수행했을 때 최대값 찾기
        for i in range(n):
            for j in range(n):
                res = max(res, board[i][j])
        return

    for i in range(4):      # 4방향
        tmp_board = move(deepcopy(board), i)
        back_tracking(tmp_board, cnt + 1)

back_tracking(board, 0)
print(res)