# 인구 이동, G5, 구현

from sys import stdin
from collections import deque

N,L,R = map(int,stdin.readline().split())
# 두 나라의 인구차이가 L ~ R

graph = []
for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))

def bfs(x, y):
    q = deque()
    q.append([x,y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = []
    temp.append((x,y))

    while q:
        a ,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:        # 국경선 열기
                if R >= abs(graph[nx][ny] - graph[a][b]) >= L:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append((nx,ny))
    return temp

res = 0

while 1:
    visited = [[0] * (N+1) for _ in range(N+1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    num = sum([graph[x][y] for x ,y in country]) // len(country)
                    # 각 칸의 인구수 조정
                    for x, y in country:
                        graph[x][y] = num
    if flag == 0:
        break
    res += 1

print(res)