# 감시 피하기, G5, 완탐-백트래킹

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = []
teacher = 0     # 총 선생의 수
for _ in range(n):
  data = list(stdin.readline().strip().split(' '))
  teacher += data.count('T')
  graph.append(data)

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<=nx<n and 0<=ny<n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':        # 찾았다
                return True
            else:
                nx += dx[i]         # 상하좌우 더 가보기
                ny += dy[i]
    return False

def sol(cnt):
    global res
    if cnt == 3:
        tmp = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    if not bfs(i, j):       # 못찾음
                        tmp += 1
        if tmp == teacher:          # 선생수만큼 반복해도 못찾음 -> YES
            res = True
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'   # 장애물 추가
                cnt += 1
                sol(cnt)
                graph[i][j] = 'X'
                cnt -= 1

res = False
sol(0)
if res:
    print("YES")
else:
    print("NO")