# 보이저 1호, S1, 구현-시뮬

from sys import stdin

n ,m = map(int, stdin.readline().split())

space = [['C'] * (m+2) for _ in range(n+2)]

for i in range(1, n+1):
    space[i] = ['C'] + list(map(str,stdin.readline().rstrip())) + ['C']

x, y = map(int, stdin.readline().split())

dx = [-1, 0, 1, 0]
dy = [0 , 1, 0, -1]      # 북동서남

P = [1, 0 ,3, 2]
Q = [3, 2, 1, 0]

direction = ['U', 'R', 'D', 'L']

res = 0
dir = 0


for i in range(4):
    nx, ny, d, time = x, y, i , 1

    while 1:
        if space[nx + dx[d]][ny + dy[d]] == 'C':
            break
        nx += dx[d]
        ny += dy[d]

        if space[nx][ny] == '/':
            d = P[d]
        elif space[nx][ny] == "\\":
            d = Q[d]
        time += 1

        if (nx, ny, d) == (x, y, i):        # 처음 출발한 지점을 동일한 방향으로 접근 -> cycle -> 무한 루프
            print(direction[i])
            print("Voyager")
            exit(0)

    if res < time:
        res = time
        dir = i

print(direction[dir])
print(res)

