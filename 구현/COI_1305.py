# 동물원의 낙타

from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    x, d = map(int,stdin.readline().split())
    arr[x] = 1

