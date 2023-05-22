# 뱀, G4, 구현 - 덱

from sys import stdin
import heapq
from collections import deque

n = int(stdin.readline())
k = int(stdin.readline())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, stdin.readline().split())
    board[a-1][b-1] = 2     # 사과는 2

l = int(stdin.readline())
# 시작은 오른쪽, 길이는 1
q = deque()         # 뱀
q.append((0,0))     # 현재 뱀은 0,0에

direction = dict()
for i in range(l):
    a, b = stdin.readline().split()
    direction[int(a)] = b

time = 0    # 시간
d = 0       # 방향 설정 변수


def turn(m):
    global d
    if m == 'L':            #왼쪽 90도 방향 회전
        d = (d-1) % 4
    else:
        d = (d+1) % 4

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]      # 동 북 서 남

x, y = 0, 0             # 시작점
board[x][y] = 1
while 1:
    time += 1
    x += dx[d]
    y += dy[d]

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if board[x][y] == 2:
        board[x][y] = 1     # 현재 좌표로 머리 위치 바꾸고
        q.append((x,y))     # 현재 위치를 q에 넣고
        if time in direction:
            turn(direction[time])
    elif board[x][y] == 0:
        board[x][y] = 1
        q.append((x,y))
        tx, ty = q.popleft()            # 꼬리 위치 빼주고
        board[tx][ty] = 0               # 꼬리 부분 0으로 바꿔줌
        if time in direction:
            turn(direction[time])
    else:
        break

print(time)