# 알파벳, G4, 그래프 - dfs()
# (0,0,)부터 시작 -> 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

from sys import stdin
from collections import deque
# deque로 풀면 시간초과 발생 -> find 하는 과정에서 O(n)
# set을 통해 중복값 제거로 O(1)

r, c = map(int, stdin.readline().split())
graph = [[] for _ in range(r)]
for i in range(r):
    graph[i] = list(map(str, stdin.readline().rstrip()))

res = 1

def bfs(x,y):
    global res
    q = set([(x, y, graph[x][y])])      # 좌표값과 해당 알파벳을 집합으로 생성
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        a, b, alpha = q.pop()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<r and 0<=ny<c and (graph[nx][ny] not in alpha):
                q.add((nx,ny,alpha + graph[nx][ny]))        # alpha에 추가해줘야 함
                res = max(res, len(alpha) + 1)
bfs(0,0)
print(res)


