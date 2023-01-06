# 달팽이, 실버3, 구현
# 런타임 에러 남 -> 이유 모름

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
x, y = n // 2, n // 2

dx = [0, 1, 0, -1]      # → ↓ ← ↑
dy = [1, 0, -1, 0]      # 좌측 대각선 위부터 시작

len = 0
cnt = 1
board[x][y] = cnt

while True:
    for i in range(4):
        for _ in range(len):
            x += dx[i]
            y += dy[i]
            cnt += 1
            board[x][y] = cnt
            if cnt == m:
                res = (x+1, y+1)
    if x == y == 0:
        break   # 쭉 돌아서 끝까지 가면 0,0에서 멈춤
    x -= 1
    y -= 1      # 좌측 대각선 위에서 시작
    len += 2    # 오른쪽으로 2, 4, 6, 8 ... 증가

for i in range(n):
    print(*board[i])
print(*res)