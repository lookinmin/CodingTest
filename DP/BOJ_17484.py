# 진우의 달 여행, S3, DP-완탐

from sys import stdin


dir = [-1, 0, 1]

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, stdin.readline().split()))

def dfs(col, row, d, low, res):
    if col == n-1:
        return min(low, res)

    for i in dir:
        if i != d:      # 두번연속 같은 방향 안됨
            if 0<=col <n and 0<=row + i <m:
                low = dfs(col + 1, row + i, i, low, res + graph[col + 1][row + i])
    return low

low = int(1e9)

for i in range(m):
    low = min(dfs(0, i, 2, low, graph[0][i]), low)

print(low)