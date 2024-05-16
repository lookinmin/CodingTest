# N과 M(11), S2
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

res = []
total = []
def dfs(depth):
    if depth == m:
        print(*res)
        return

    tmp = 0         # 중복 제거 용, set() 보다 훨씬 시간 복잡도 측면에서 효율적임
    for i in range(n):
        if tmp != arr[i]:
            res.append(arr[i])
            tmp = arr[i]
            dfs(depth + 1)
            res.pop()

dfs(0)