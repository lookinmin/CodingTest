# n과m (7), S3
from sys import stdin

n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

res = []
def dfs(depth):
    if depth == m:
        print(*res)
        return

    for i in range(n):
        res.append(arr[i])
        dfs(depth + 1)
        res.pop()

dfs(0)