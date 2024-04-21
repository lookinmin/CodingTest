# 근손실, S3
from sys import stdin
n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
visited = [0] * n

now = 500
cnt = 0

def dfs(depth):
    global cnt, now
    if depth == n:
        cnt += 1
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1

                if now + arr[i] - k >= 500:
                    now += arr[i] - k
                    dfs(depth + 1)
                    now -= arr[i] - k
                    visited[i] = 0
                else:
                    visited[i] = 0

dfs(0)
print(cnt)