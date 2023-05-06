# 뱀과 사다리 게임, G5, 그래프

from sys import stdin
from collections import deque

board = [0] * 101
visited = [0] * 101

n, m = map(int, stdin.readline().split())
stair = dict()              # 계단과 뱀을 딕셔너리 형태로 받기
for i in range(n):
    a, b = map(int, stdin.readline().split())
    stair[a] = b

snake = dict()
for i in range(m):
    a, b = map(int, stdin.readline().split())
    snake[a] = b

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        x = q.popleft()

        if x == 100:
            print(board[x])
            break
        for i in range(1, 7):
            nx = x + i
            if nx <= 100 and not visited[nx]:
                if nx in stair.keys():      # 딕셔너리 형태로 받아, keys()안에 값이 있으면
                    nx = stair[nx]          # 해당 도착지점으로 nx를 이동
                if nx in snake.keys():
                    nx = snake[nx]
                if not visited[nx]:
                    visited[nx] = 1
                    board[nx] = board[x] + 1
                    q.append(nx)

bfs(1)