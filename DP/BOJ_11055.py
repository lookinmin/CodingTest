# 가장 큰 중가 부분 수열, 실버2, DP
from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
d = [1] * n
d[0] = a[0]

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j]+a[i])
        else:
            d[i] = max(d[i], a[i])

print(max(d))
