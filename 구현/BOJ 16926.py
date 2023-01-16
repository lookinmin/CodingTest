# 배열 돌리기 1, 실버1, 구현

from sys import stdin

n, m, r = map(int,stdin.readline().split())
board = []
for i in range(n):
    board.append(list(map(int,stdin.readline().split())))

for _ in range(r):
    for i in range(min(n,m)//2):
        x, y = i, i
        tmp = board[x][y]
        # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위설정
        for j in range(i+1, n-i):
            x = j
            preTmp = board[x][y]
            board[x][y] = tmp
            tmp = preTmp

        for j in range(i+1, m - i):
            y = j
            preTmp = board[x][y]
            board[x][y] = tmp
            tmp = preTmp

        for j in range(i+1, n-i):
            x = n - j -1
            preTmp = board[x][y]
            board[x][y] = tmp
            tmp = preTmp

        for j in range(i+1, m -i):
            y = m - j - 1
            preTmp = board[x][y]
            board[x][y] = tmp
            tmp = preTmp

for i in range(n):
    print(*board[i])
