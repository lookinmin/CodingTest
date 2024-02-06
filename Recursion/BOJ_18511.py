# 큰 수 구성하기, S5

from sys import stdin
from itertools import product


n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

l = str(n)
candidates = []

for i in range(len(l), 0, -1):
    tmp = list(product(arr, repeat = i))
    for num in tmp:
        candidates.append(int(''.join(map(str, num))))

for num in sorted(candidates)[::-1]:
    if num <= n:
        print(num)
        exit()
