# 미로만들기, S2

from sys import stdin

n = int(stdin.readline())
moves = stdin.readline().rstrip()
dx = [-1 ,0, 1, 0]
dy = [0, 1, 0, -1]

dir = 2 # 남쪽
pos = [0, 0]    # 현 위치
xList = [0]
yList = [0]

for move in moves:
    if move == 'L':
        dir = (dir - 1) % 4
    elif move == 'R':
        dir = (dir + 1) % 4
    else:
        x, y = pos
        nx, ny = x + dx[dir], y + dy[dir]
        xList.append(nx)
        yList.append(ny)
        pos = [nx, ny]

max_x, min_x, max_y, min_y = max(xList), min(xList), max(yList), min(yList)     # 총 이동 거리의 최소와 최대
N, M = max_x - min_x + 1, max_y - min_y + 1     # 길이
graph = [['#'] * M for _ in range(N)]

sx, sy = abs(min_x), abs(min_y)

for i in range(len(xList)):
    graph[sx + xList[i]][sy + yList[i]] = '.'

for line in graph:
    print("".join(line))