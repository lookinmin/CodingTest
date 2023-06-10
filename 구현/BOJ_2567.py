# 색종이 - 2, S4, 구현
# 둘레 구하기


from sys import stdin

n = int(stdin.readline())

board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

dx = [-1, 1, 0 ,0]
dy = [0 ,0, -1, 1]

# 모서리에선 + 2

res = 0

for x in range(1, 101):
    for y in range(1, 101):
        if board[x][y] == 1:
            cnt = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if board[nx][ny] == 1:
                    cnt += 1
            if cnt == 3:            # 그냥 변
                res += 1
            elif cnt == 2:          # 모서리
                res += 2

print(res)