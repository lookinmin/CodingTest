# 도전 숫자왕, S2
from sys import stdin
from itertools import combinations
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = sum(arr)

num = set()

for i in range(1, n + 1):
    for tmp in combinations(arr, i):
        num.add(sum(tmp))

print(m - len(num))