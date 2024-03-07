# 최고의 피자, S3, 그리디
from sys import stdin
n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
c = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

price = a
total = c
res = int(total / price)
arr.sort(reverse=True)

for i in range(n):
    price += b
    total += arr[i]
    res = max(res, int(total / price))

print(res)