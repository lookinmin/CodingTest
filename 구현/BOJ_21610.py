# 마법사 상어와 비바라기, G5, 구현
# 바구니에 저장할 수 있는 물의 양에는 제한이 없다
# 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다

from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

move = []
for i in range(m):
    d, s = map(int, stdin.readline().split())
    move.append((d,s))

dx8 = ["empty", 0, -1, -1, -1, 0, 1, 1, 1]
dy8 = ["empty", -1, -1, 0, 1, 1, 1, 0, -1]

dx4 = [-1, -1, 1, 1]
dy4 = [-1, 1, -1, 1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for d, s in move:
    moved_clouds = []
    for x ,y in clouds:
        nx = (x + dx8[d] * s) % n   # 구름 이동 좌표는 연결
        ny = (y + dy8[d] * s) % n
        graph[nx][ny] += 1
        moved_clouds.append((nx,ny))

    for x, y in moved_clouds:
        cnt = 0
        for i in range(4):
            nx = x + dx4[i]
            ny = y + dy4[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] > 0 :
                cnt += 1
            else:
                continue
        graph[x][y] += cnt

    new_clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) in moved_clouds or graph[i][j] < 2:
                continue
            graph[i][j] -= 2
            new_clouds.append((i,j))

    clouds = new_clouds

res = 0
for i in range(n):
    for j in range(n):
        res += graph[i][j]


print(res)