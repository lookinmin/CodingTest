# 스티커, S1, DP

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    board = []
    for _ in range(2):
        board.append(list(map(int, stdin.readline().split())))



    for i in range(1, n):
        if i == 1:
            board[0][i] += board[1][i-1]
            board[1][i] += board[0][i-1]
        else:
            board[0][i] += max(board[1][i-1], board[1][i-2])        # 대각선 바로 이전꺼, 혹은 그전꺼
            board[1][i] += max(board[0][i-1], board[0][i-2])

    print(max(board[0][n-1], board[1][n-1]))


