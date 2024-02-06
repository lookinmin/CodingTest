# 좋은 구간, S4

from sys import stdin
L = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))
n = int(stdin.readline())

if n in arr:
    print(0)
    exit()

start, end = 0, 0
for i in range(L - 1):
    if arr[i] < n < arr[i + 1]:
        start = arr[i] + 1
        end = arr[i + 1] - 1
        break
else:
    if n <= arr[0]:
        start = 1
        end = arr[0] - 1
res = []
for i in range(start, end):
    for j in range(i + 1, end + 1):
        if i <= n <= j:
            res.append([i, j])

print(len(res))