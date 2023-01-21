# 부분수열의 합, S2, 브루트포스, 백트래킹
from sys import stdin
import itertools
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
cnt = 0
for i in range(1, n+1):
    nCr = itertools.combinations(arr, i)
    for j in nCr:
        if sum(j) == s:
            cnt += 1

print(cnt)