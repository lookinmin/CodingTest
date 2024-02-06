# 주몽, S4
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort()

start = 0
end = n - 1
cnt = 0
while start < end:
    if arr[start] + arr[end] == m:
        cnt += 1
        start += 1
    elif arr[start] + arr[end] < m:
        start += 1
    else:
        end -= 1
print(cnt)