# 사탕게임, S2, 구현 - 완탐

from sys import stdin

n = int(stdin.readline())
arr=[list(stdin.readline().rstrip()) for _ in range(n)]

res = 0

def check_row():
    global res

    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1     # 초기화

def check_col():
    for i in range(n):
        global res

        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
                res = max(cnt, res)
            else:
                 cnt = 1

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:                # 가로로 변경
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            check_row()
            check_col()
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]         # 바꿔준거 돌려놔야됨
        if arr[j][i] != arr[j+1][i]:                # 세로로 변경
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            check_row()
            check_col()
            arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]

print(res)