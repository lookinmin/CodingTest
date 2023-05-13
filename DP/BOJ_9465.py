# 스티커, S1, DP

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline().rstrip())
    board = []
    for _ in range(2):
        board.append(list(map(int, stdin.readline().split())))

    board[0][1] += board[1][0]
    board[1][1] += board[0][0]

    for i in range(2, n):
        board[0][i] += max(board[1][i-1], board[1][i-2])        # 대각선 바로 이전꺼, 혹은 그전꺼
        board[1][i] += max(board[0][i-1], board[0][i-2])

    res = max(board[0][n-1], board[1][n-1])
    print(res)


