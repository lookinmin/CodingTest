# Puyo Puyo, G4, 구현

from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [[] for _ in range(12)]
for i in range(12):
    graph[i] = list(stdin.readline().rstrip())

res = 0
def bfs(value, x,y):
    q = deque()
    q.append([x,y])

    visited = [[-1]*6 for _ in range(12)]
    visited[x][y] = 0
    check = [[x,y]]

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<12 and 0<=ny<6 and visited[nx][ny] == -1 and graph[nx][ny] == value:
                    visited[nx][ny] = 0
                    q.append([nx,ny])
                    check.append([nx,ny])
    if len(check) >= 4:     # 방문값이 4개 이상
        for x, y in check:
            graph[x][y] = '.'
        return True
    return False

flag = True

while flag:
    flag = False
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] != '.':
                flag |= bfs(graph[i][j], i, j)          # |= -> merge & update

    if flag:        # 연쇄가 일어남 -> 빈공간 떨어지기
        res += 1
        for j in range(6):
            for i in range(10, -1, -1):
                for k in range(11, i, -1):      # i,j보다 한칸 밑에
                    if graph[i][j] != '.' and graph[k][j]== '.':        #현재 내가 .이 아니고, 한칸 밑이 . 이라면
                        graph[i][j], graph[k][j] = graph[k][j], graph[i][j]     # 내 값을 한칸 밑으로 내리고 내 값을 .으로
                        break
print(res)
