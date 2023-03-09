# 바스켓맨

from sys import stdin

n, k, d = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
res = []
for i in arr:
    if i >= k:
        res.append(i)

print("{} {}".format(len(res), max(res)))