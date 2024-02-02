from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
# 어차피 n <= 100

res = 0

for i in range(2, max(arr) + 1):
    cnt = 0
    for j in range(n):
        if arr[j] % i == 0:
            cnt += 1
    res = max(res, cnt)

print(res)