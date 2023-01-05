# 빙고, 실버4, 구현-시뮬레이션

from sys import stdin
board = [[0]*5 for _ in range(5)]
simpan = [[0]*5 for _ in range(5)]

cnt = 0

for i in range(5):
    board[i] = list(map(int, stdin.readline().split()))

for i in range(5):
    simpan[i] = list(map(int, stdin.readline().split()))

def sol(arr):
    bingo = 0
    for i in range(5):      # 가로 빙고
        if sum(arr[i]) == 0:
            bingo += 1
    for i in range(5):      # 세로 빙고
        tmp = 0
        for j in range(5):
            if arr[j][i] == 0:
                tmp += 1
        if tmp == 5:
            bingo += 1

    # 대각선 빙고
    tmp_up = []
    tmp_down = []
    for i in range(5):
        tmp_up.append(arr[i][i])
        tmp_down.append(arr[i][4-i])
    if sum(tmp_up) == 0:
        bingo += 1
    if sum(tmp_down) == 0:
        bingo += 1

    return bingo


for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):
                if simpan[i][j] == board[k][h]:
                    board[k][h] = 0
                    cnt += 1
                if cnt >= 12:
                    if sol(board) >= 3:
                        print(cnt)
                        exit()
