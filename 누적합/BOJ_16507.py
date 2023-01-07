# 어두운 건 무서워, 실버1, 누적합
from sys import stdin

r,c,q = map(int, stdin.readline().split())

board = [list(map(int, input().split())) for _ in range(r)]
sum_arr = [[0] * (c + 1) for _ in range(r + 1)]             # 누적합 배열도 2차원으로 선언

for i in range(1, r+1):
    for j in range(1, c+1):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] + board[i-1][j-1] - sum_arr[i-1][j-1]     # 이차원 리스트 누적합 공식

for i in range(q):
    r1, c1, r2, c2 = map(int, stdin.readline().split())
    res = sum_arr[r2][c2] - sum_arr[r1-1][c2] - sum_arr[r2][c1-1] + sum_arr[r1-1][c1-1]
    print(res//((r2-r1+1)*(c2-c1+1)))