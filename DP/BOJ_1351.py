# 무한 수열, G5, Dp

from sys import stdin
n, p, q = map(int, stdin.readline().split())

# 7, 2, 3
data = {}
# data[i] = data[i/p] + data[i/q]
data[0] = 1

def dfs(n):
    if n in data:
        return data[n]

    data[n] = dfs(n//p) + dfs(n//q)
    return data[n]
# 시간초과가 있는 무한 수열탐색 -> 재귀형태로 탐색
print(dfs(n))