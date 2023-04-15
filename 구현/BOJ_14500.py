# 테트로미노, G4, 구현-브루트포스

from sys import stdin

n,m = map(int, stdin.readline().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]             # 대각선 진행은 없으니까
dy = [0,0,-1,1]             # ㅗ 모양 제외, 결국 dfs 4번 하면 모든 모양 나옴
res = 0
max_val = max(map(max, graph))      # 현재 그래프에서 가장 큰 값

def dfs(x,y, idx, total):       # idx = 현재 몇개째 탐색 중인지
    global res
    if res >= total + max_val * (3 - idx):      #
        return
    if idx == 3:            # 4개 다 확인 했으면
        res = max(res, total)       # res 최신화
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if idx == 1:            # ㅗ모양 만들기
                    visited[nx][ny] = 1
                    dfs(x,y, idx+1,total + graph[nx][ny])   # nx가 아닌 x,y에서 dfs 한번 더 수행
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx,ny,idx+1,total + graph[nx][ny])
                visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,0,graph[i][j])
        visited[i][j] = 0

print(res)