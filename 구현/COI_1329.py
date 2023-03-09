# 코로나1

from sys import stdin
n, m = map(int, stdin.readline().split())
board = [[0]*m for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 9:
            cnt1 += 1
        elif 2 <= board[i][j] <= 8:
            cnt2 += 1
print(cnt1)
print(cnt2)