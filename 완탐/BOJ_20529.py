# 가장 가까운 세 사람의 심리적 거리, S1
from sys import stdin
from itertools import combinations

T = int(stdin.readline())

def check(a, b):
    tmp = 0
    for i, j in zip(a, b):
        if i != j:
            tmp += 1
    return tmp

for _ in range(T):
    n = int(stdin.readline())
    arr = list(stdin.readline().split())

    if n > 32:
        print(0)
        continue
    else:
        res = 13
        comb = combinations(arr, 3)
        for a, b, c in comb:
            dist = 0
            dist += check(a, b)
            dist += check(a, c)
            dist += check(b, c)

            res = min(res, dist)
        print(res)