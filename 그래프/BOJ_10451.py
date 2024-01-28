# 순열 사이클, S3, 그래프

from sys import stdin
import sys
sys.setrecursionlimit(10**8)

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    origin = [i for i in range(1, n+1)]
    arr = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(n+1)]

    for i in range(n):
        graph[origin[i]].append(arr[i])

    visited = [0] * (n+1)

    def dfs(s):
        visited[s] = 1
        for node in graph[s]:
            if not visited[node]:
                visited[node] = 1
                dfs(node)

    cnt = 0
    for i in range(1 ,n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)

