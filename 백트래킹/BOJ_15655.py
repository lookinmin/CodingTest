# N과M (6), S3
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int,stdin.readline().split())))

visited = [0] * n
res= []
def dfs(depth, idx):
    if depth == m:
        print(*res)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            res.append(arr[i])
            dfs(depth + 1, i + 1)
            res.pop()
        visited[i] = 0

dfs(0, 0)