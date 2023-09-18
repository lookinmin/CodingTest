# 봄버맨, S1, 구현-retry

from sys import stdin
from collections import deque
# 폭탄은 3초 후 폭발
# 0초 = 특정 위치에 폭탄
# 1초 = X
# 2초 = 특정 위치가 아닌 모든 곳에 폭탄
# 3초 = 0초에 폭탄이 위치한 곳 bomb

def loc_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i, j))

def full_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():      # 폭탄 터뜨리기
    while bomb:
        x, y = bomb.popleft()
        graph[x][y] = '.'       # 터졌으니까 빈 공간으로 대체

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] == "O":
                    graph[nx][ny] = '.'


r, c, n = map(int,stdin.readline().split())
# n초가 흐른 후 격자판의 상태 구하기

graph = [[] for _ in range(r)]

for i in range(r):
    graph[i] = list(stdin.readline().rstrip())

n -= 1

while n:
    bomb = deque()
    loc_bomb()
    full_bomb()

    n -= 1
    if n == 0:
        break

    bfs()
    n -= 1


for row in graph:
    print("".join(row))
