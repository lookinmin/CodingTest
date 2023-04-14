# 경쟁적 전염
# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식


from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
virus = []
for i in range(n):
    graph[i] = list(map(int ,stdin.readline().split()))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))   # 바이러스의 종류, 좌표를 순서대로 입력

s, x, y = map(int, stdin.readline().split())


def bfs(s,x,y):
    q = deque(virus)

    cnt = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        if cnt == s:
            break
        for _ in range(len(q)):     # pop하기 위한 단계
            value, a, b, = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[a][b]
                        q.append((graph[nx][ny],nx,ny))
        cnt += 1
    return graph[x-1][y-1]

virus.sort()        # 낮은 수의 바이러스 부터
print(bfs(s,x,y))