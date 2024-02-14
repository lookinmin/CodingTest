# 크로스워드, S2

from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = stdin.readline().rstrip()

words = []

for i in range(n):
    tmp = ''
    for j in range(m):
        if board[i][j] == '#':
            if len(tmp) > 1:
                words.append(tmp)
            tmp = ''
        else:
            tmp += board[i][j]

    if len(tmp) > 1:
        words.append(tmp)

for j in range(m):
    tmp = ''
    for i in range(n):
        if board[i][j] == '#':
            if len(tmp) > 1:
                words.append(tmp)
            tmp = ''
        else:
            tmp += board[i][j]

    if len(tmp) > 1:
        words.append(tmp)

print(sorted(words)[0])