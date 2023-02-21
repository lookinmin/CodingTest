# 치즈, G4, 구현-그래프-시뮬레이션
# 1. 구멍찾기
from sys import stdin
from collections import deque
n,m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))


ans = []

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0 <= nx <n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    graph[nx][ny] = 0   # 치즈 -> 공기
                    visited[nx][ny] = 1
                    cnt += 1
                    # 공기와 접촉한 칸은 queue에 append하지 앉아야 함! -> 안쪽까지 녹으니까
    ans.append(cnt)
    return cnt

time = 0

while 1:
    time += 1
    visited = [[0] * m for _ in range(n)]       # 방문을 매번 초기화해줘야 함
    cnt = bfs(0,0)
    if cnt == 0:
        break

print(time - 1)
print(ans[-2])