# N과M (10), S2
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

visited = [0] * n
total = set()
res = []
def dfs(depth, idx):
    if depth == m:
        if tuple(res) not in total:
            print(*res)
            total.add(tuple(res))
            return

    for i in range(idx, n):
        if not visited[i]:
            res.append(arr[i])
            visited[i] = 1
            dfs(depth + 1, i)
            res.pop()
            visited[i] = 0

# ----------------------------------

def tracking(depth, idx):
    if depth == m:
        print(*res)
        return
    tmp = 0     # 비교를 위한 값, 중복 방지

    for i in range(idx, n):
        if not visited[i] and tmp != arr[i]:
            res.append(arr[i])
            visited[i] = 1
            tmp = arr[i]
            tracking(depth + 1, i + 1)
            visited[i] = 0
            res.pop()

dfs(0, 0)
tracking(0, 0)
