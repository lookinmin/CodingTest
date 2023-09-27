# 내리막 길, G3, DFS + DP

from sys import stdin
import sys
sys.setrecursionlimit(10 ** 8)

m, n = map(int, stdin.readline().split())
graph = [[] for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(m):
    graph[i] = list(map(int, stdin.readline().split()))

# 단순 dfs만으로는 모든 경우의 수를 탐색하는 브루트포스가 되기 때문에 500*500 에서 시간초과가 발생한다
# 도착 지점까지 경우의 수 = 임의의 점들에서 도착지점까지의 경우의 수

def dfs(x, y):
    if x == m-1 and y == n-1:       # 도착지점에 도달 -> 한가지 경우 리턴
        return 1

    if dp[x][y] != -1:      # 이미 방문한 적이 있음
        return dp[x][y]     # 그 위치(임의의 점)에서 출발하는 경우의 수 리턴

    ways = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and graph[x][y] > graph[nx][ny]:
            ways += dfs(nx, ny)

    dp[x][y] = ways     # 임의의 점까지 도달하는 경우의 수를 변화
    return dp[x][y]

print(dfs(0,0))
