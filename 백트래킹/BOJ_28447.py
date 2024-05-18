# 마라탕 재료 고르기, S2
from sys import stdin
from itertools import combinations
n, k = map(int, stdin.readline().split())
gredients = []

for _ in range(n):
    gredients.append(list(map(int, stdin.readline().split())))

if k == 1:
    print(0)
    exit()

res = []
for comb in combinations([i for i in range(n)], k):
    tmp = 0
    
    for pick in combinations(comb, 2):
        tmp += gredients[pick[0]][pick[1]]
    
    res.append(tmp)
print(max(res))