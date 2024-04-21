# N과 M(5)
from sys import stdin
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()
visited = [0] * n
out = []

def backtracking(depth, n, m):
    if depth == m:
        print(*out)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            out.append(arr[i])
            backtracking(depth + 1, n, m)
            out.pop()
            visited[i] = 0

backtracking(0, n, m)