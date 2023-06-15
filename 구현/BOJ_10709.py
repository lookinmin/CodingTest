# 기상캐스터, S5, 구현

from sys import stdin

h, w = map(int, stdin.readline().split())

graph = [[] for _ in range(h)]

for i in range(h):
    graph[i] = list(stdin.readline().rstrip())

board = [[-1]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'c':
            board[i][j] = 0
            cnt = 1
            j += 1
            while 1:
                if j == w:
                    break
                board[i][j] = cnt
                cnt += 1
                j += 1


for i in range(h):
    print(*board[i])