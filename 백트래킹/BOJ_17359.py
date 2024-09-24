# S2, 전구 길만 걷자
from sys import stdin
from itertools import permutations

n = int(input())

bulbs = [input().strip() for _ in range(n)]
base = 0

for bulb in bulbs:
    for i in range(len(bulb) - 1):
        if bulb[i] != bulb[i + 1]:
            base += 1

res = float('inf')
idx = list(range(n))

for perm in permutations(idx):
    cnt = 0
    
    for i in range(n - 1):
        if bulbs[perm[i]][-1] != bulbs[perm[i + 1]][0]:
            cnt += 1

    res = min(res, cnt)

print(base + res)