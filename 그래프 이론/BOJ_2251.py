# 물통, G5, 그래프
from sys import stdin
from collections import deque

a, b, c = map(int, stdin.readline().split())
# 3개의 물통에서 물을 한번 옮겨담는 경우의 수 = 6
# BFS로 완전 탐색 구현 (모든 경우의 수)
# visited 배열의 크기 = (A+1) * (B+1) 의 2차원 배열

visited = [[0] * (b+1) for _ in range(a+1)]
visited[0][0] = 1

res = []
q = deque()
q.append((0, 0))

def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append((x,y))

def bfs():
    while q:
        # x, y = A,B에 있는 물, z = C에 있는 물
        x, y = q.popleft()
        z = c - x - y
        if x == 0:
            res.append(z)

        water = min(x, b-y)
        pour(x - water, y + water)  # A->B로 물 이동

        water = min(x, c-z)
        pour(x-water, y)            # A->C로 물 이동

        water = min(y, c-z)
        pour(x, y-water)            # B->C

        water = min(y, a-x)
        pour(x+water, y-water)      # B->A

        water = min(z, a-x)
        pour(x+water, y)            # C->A

        water = min(z, b-y)
        pour(x, y+water)            # C->B

bfs()
res.sort()
print(*res)
