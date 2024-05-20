# 1, 2, 3 더하기 2, S1
from sys import stdin
n, k = map(int, stdin.readline().split())

arr = [1, 2, 3]
total = set()
def dfs(value, tmp):
    if value == n:
        total.add(tuple(tmp))
        return

    if value + 1 <= n:
        dfs(value + 1, tmp + [1])
    if value + 2 <= n:
        dfs(value + 2, tmp + [2])
    if value + 3 <= n:
        dfs(value + 3, tmp + [3])

dfs(0, [])

if len(total) < k:
    print(-1)
else:
    res = sorted(list(total))[k-1]
    print(*res, sep='+')
