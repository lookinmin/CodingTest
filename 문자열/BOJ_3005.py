# 크로스워드 퍼즐 쳐다보기, S2

from sys import stdin
n, m = map(int, stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = stdin.readline().rstrip()

tmp = []
for i in range(n):
    word = ''
    for j in range(m):
        if board[i][j] != '#':
            word += board[i][j]
        else:
            if len(word) < 2:
                word = ''
                pass
            else:
                tmp.append(word)
                word = ''
    if len(word) >= 2:
        tmp.append(word)

for j in range(m):
    word = ''
    for i in range(n):
       if board[i][j] != '#':
           word += board[i][j]
       else:
           if len(word) < 2:
               word = ''
               pass
           else:
               tmp.append(word)
               word = ''
    if len(word) >= 2:
        tmp.append(word)
print(sorted(tmp)[0])
