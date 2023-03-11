# 연구소, G4, 구현-그래프
# 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져 나갈 수 있다
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
# 0 = 빈칸, 1 = 벽, 2 = 바이러스
# 안전 영역의 최댓값

from sys import stdin
from collections import deque
import copy



def bfs():               # 바이러스 퍼지는거 만들기
    q = deque()
    tmp_graph = copy.deepcopy(graph)                        # 매번 어떤 경우가 최선인지 알기위해 deepcopy후 계산
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:                        # 바이러스인 상태를 전부 큐에 넣기
                q.append((i, j))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny] == 0:      # 0인 상태를
                tmp_graph[nx][ny] = 2                               # 바이러스 상태로 만들고
                q.append((nx,ny))                                   # 큐에넣기

    cnt = 0                     # 안전영역 수 확인할 변수
    global res
    for i in range(n):
        cnt += tmp_graph[i].count(0)        # 안전영역 개수 세기
    res = max(res,cnt)

def makeWall(x):
    if x == 3:
        bfs()       # 벽 3개 지었으면 bfs() 수행해서 안전영역 크기 확인
        return

    for i in range(n):              # 백트래킹 방식으로 0인 위치를 벽으로 만들기
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(x + 1)         # 벽 하나 만들면서 재귀적으로 수행
                graph[i][j] = 0         # 만든 벽 초기화 해야함


n, m = map(int, stdin.readline().split())
graph = [[0]*m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

res = 0
makeWall(0)

print(res)
