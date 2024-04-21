# 눈덩이 굴리기, S3
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
res = 0
now = 1

def dfs(depth, idx, now):
    global res
    now += arr[idx]

    if depth == m:
        res = max(res, now)
        return
    if idx == n - 1:
        res = max(res, now)
        return

    if idx + 1 < n:
        dfs(depth + 1, idx + 1, now)

    if idx + 2 < n:
        dfs(depth + 1, idx + 2, now // 2)

dfs(1, 0, now)
if n > 1:
    dfs(1, 1, 0)    # 바로 한칸 앞에 던지는 건가?

print(res)