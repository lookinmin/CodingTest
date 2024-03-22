# 성 지키기
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(stdin.readline().rstrip())

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if board[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_cnt = 0
col_cnt = 0

for i in range(n):
    if row[i] == 0:
        row_cnt += 1

for i in range(m):
    if col[i] == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))