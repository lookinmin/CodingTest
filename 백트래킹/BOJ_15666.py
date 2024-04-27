# N과 M (12), S2
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = sorted(set(list(map(int, stdin.readline().split()))))
res = []

def dfs(depth, idx):
    if depth == m:
        print(*res)
        return

    for i in range(idx, len(arr)):
        res.append(arr[i])
        dfs(depth + 1, i)
        res.pop()

dfs(0, 0)
