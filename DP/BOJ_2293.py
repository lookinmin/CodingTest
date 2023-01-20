# 동전 1, G5, DP

from sys import stdin
n, k = map(int, stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

d = [0] * (k+1)
d[0] = 1
# d[1] = 합이 1원, d[2] = 합이 2원

for i in arr:                       # 각각의 화폐 단위
    for j in range(i, k+1):         # 특정 가치의 동전을 썼을 때 합이 j원
        if j - i >= 0:
            d[j] += d[j-i]

print(d[k])