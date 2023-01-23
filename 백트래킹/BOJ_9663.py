# N-QUEEN, G4, 백트래킹 - 완탐
# n*n크기 체스판, 퀸 n개 놓는 방법의 수
from sys import stdin
n = int(stdin.readline())

ans = 0
row = [0] * n   # 어차피 한 column에 퀸 들어오면 절대 못들어옴 1차원으로 가능

def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):    # 같은 열이거나 대각선일 때
            return False
    return True

def nQueens(x):
    global ans
    if x == n:      # 끝까지 갔으면 종료
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i      # [x, i] 에 퀸
            if promising(x):
                nQueens(x + 1)

nQueens(0)
print(ans)
