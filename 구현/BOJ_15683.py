# 감시, G4, 구현-완탐
# 방향에 있는 칸 전체, CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향
import copy
from sys import stdin


n,m= map(int,stdin.readline().split())
graph = [[] for _ in range(n)]

cctv = []
res = int(1e9)         # 0으로 남은 공간 찾기 -> dfs

mode = [                        # 각 cctv 번호에 해당하는 방향정보를 담은 배열
    [],
    [[0],[1],[2],[3]],          # 0이 북쪽, 1이 동쪽, 2가 남쪽, 3이 서쪽
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2], [0,1,3], [1,2,3], [0,2,3]],
    [[0,1,2,3]]
]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j], i, j])


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fill(graph, mode,x,y):
    for i in mode:      # cctv 방향에 따라
        nx = x
        ny = y
        while 1:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 6:
                if graph[nx][ny] == 0:        # 다른 cctv값을 바꿔버리면 안되니까 0면 바꾼다.
                    graph[nx][ny] = -1
            else:
                break

def dfs(depth, graph):
    global res
    if depth == len(cctv):          #cctv 개수 만큼 탐색하기, 탐색 완료
        cnt = 0
        for i in range(n):
            cnt += graph[i].count(0)        # 해당 열에서 0의 값(사각지대 수) 찾기
        res = min(res, cnt)
        return

    tmp = copy.deepcopy(graph)
    cctv_mode, x, y = cctv[depth]
    for i in mode[cctv_mode]:
        fill(tmp, i, x, y)          # 복사한 그래프와 mode, 좌표를 넘겨줌
        dfs(depth+1, tmp)           # 복사한 그래프에 대해 재귀적으로 dfs수행
        tmp = copy.deepcopy(graph)  # 복사한 그래프 초기화

dfs(0, graph)
print(res)
