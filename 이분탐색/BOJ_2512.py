# 예산, S3, 이분탐색

from sys import stdin
n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
m = int(stdin.readline().rstrip())

start = 0
end = max(arr)


while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i

    if total > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)