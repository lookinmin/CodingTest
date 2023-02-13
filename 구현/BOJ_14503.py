# 로봇 청소기, G5, 구현-시뮬레이션
# 0 = 청소되지 않은 빈칸, 1 = 벽

from sys import stdin
n,m = map(int, stdin.readline().split())
room = [[0]*m for _ in range(n)]
x, y, d= map(int, stdin.readline().split())
for i in range(n):
    room[i] = list(map(int, stdin.readline().split()))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4       # 왼쪽으로 한칸 돌림
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                x = nx      # 현 위치로 초기화
                y = ny
                flag = 1
                break

    if flag == 0:   # 네 방향 모두 청소 불가능
        if room[x - dx[d]][y-dy[d]] == 1:       # 후진했는데 벽
            print(cnt)
            break
        else:
            x, y = x - dx[d], y - dy[d]         # 벽 아니면 현위치 초기화