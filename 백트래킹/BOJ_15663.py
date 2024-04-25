# N과 M(9), S2
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

visited = [0] * n
res = []
total = set()
def dfs(depth):
    if depth == m:
        if tuple(res) not in total:
            total.add(tuple(res))
            print(*res)
            return

    for i in range(n):
        if not visited[i]:
            res.append(arr[i])
            visited[i] = 1
            dfs(depth + 1)
            visited[i] = 0
            res.pop()

dfs(0)