# 겉넓이 구하기, S2
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

res = n * m * 2
left = 0
front = 0

for i in range(n):
    for j in range(m):
        if j == 0:
            left += board[i][j]
        else:
            if board[i][j-1] < board[i][j]:
                left += board[i][j] - board[i][j-1]

for j in range(m):
    for i in range(n):
        if i == 0:
            front += board[i][j]
        else:
            if board[i - 1][j] < board[i][j]:
                front += board[i][j] - board[i - 1][j]

print(res + 2*left + 2*front)