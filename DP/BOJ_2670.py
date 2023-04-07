# 연속부분최대곱, S4, DP

from sys import stdin

n = int(stdin.readline())

arr = []
for _ in range(n):
    arr.append(float(stdin.readline().rstrip()))



for i in range(1, n):
    arr[i] = max(arr[i], arr[i] * arr[i-1])

print("{:.3f}".format(max(arr)))
