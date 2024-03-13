# 카드 놓기, S4, 완탐
from sys import stdin
from itertools import permutations

n = int(stdin.readline())
k = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))

perm = list(permutations(arr, k))

res = set()
for tmp in perm:
    num = ''
    for w in tmp:
        num += str(w)
    res.add(int(num))

print(len(res))
