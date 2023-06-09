# 등수 구하기, S4, 구현

from sys import stdin

n, new, p = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

res = []

if len(arr) >= p and min(arr) >= new:
    print(-1)
else:
    arr.append(new)
    arr.sort(reverse=True)
    print(arr.index(new) + 1)