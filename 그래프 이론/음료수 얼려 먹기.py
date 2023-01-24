# 음료수 얼려먹기, 그래프 예제 - connected component 찾기
# 총 생기는 아이스크림 수
from sys import stdin
N, M = map(int, stdin.readline().split())
graph = []
# 모든 지점에 대해 dfs 활용
for i in range(N):
    graph.append(list(map(int, stdin.readline().strip())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

res = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            res += 1

print(res)

