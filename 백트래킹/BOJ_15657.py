# N과M(8), S3
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
# 오름차순 출력
res = []
def dfs(idx):
    if len(res) == m:
        print(*res)
        return

    for i in range(idx, n):
        res.append(arr[i])
        dfs(i)
        res.pop()

dfs(0)