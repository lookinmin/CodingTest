# 수 고르기, G5, 정렬-투포인터

from sys import stdin

n, m = map(int, stdin.readline().split())

arr = list(int(stdin.readline().rstrip()) for _ in range(n))

arr.sort()

start = 0
end = 0

res = int(2e9)

while start <= end and end < n:
    if arr[end] - arr[start] < m:
        end += 1

    else:
        res = min(res, arr[end] - arr[start])
        start += 1

print(res)