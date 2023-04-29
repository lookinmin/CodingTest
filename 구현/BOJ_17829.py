# 222-풀링, S2, 구현

from sys import stdin

n = int(stdin.readline())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, stdin.readline().split()))

def make(n, x, y):
    mid = n // 2
    if n == 2:
        res = [board[x][y], board[x+1][y], board[x][y+1],board[x+1][y+1]]
        res.sort(reverse=True)
        return res[1]
    lt = make(mid, x, y)
    rt = make(mid, x + mid, y)
    lw = make(mid, x, y+mid)
    rw = make(mid, x+mid, y+mid)

    res = [lt, rt, lw, rw]
    res.sort(reverse=True)
    return res[1]

ans = make(n, 0, 0)
print(ans)
