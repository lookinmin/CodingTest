# 차이를 최대로, S2, 백트래킹, 완탐

from sys import stdin
from itertools import permutations
N = int(stdin.readline())
# N의 범위가 3<= N <=8 이므로 완탐

arr = list(map(int,stdin.readline().split()))
per = permutations(arr)
res = []

for i in per:       # 가능한 모든 순열을 매번 return
    tmp = 0
    for j in range(len(i) - 1):
        tmp += abs(i[j] - i[j+1])

    res.append(tmp)

print(max(res))
