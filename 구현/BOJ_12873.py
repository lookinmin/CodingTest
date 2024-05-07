# 기념품, S3
n = int(input())

from collections import deque
# 원형 큐

arr = deque([i for i in range(1, n + 1)])

cnt = 1
for i in range(n - 1):
    num = (cnt**3) % len(arr)
    if num == 1:
        arr.popleft()
    else:
        arr.rotate(-(num - 1))
        arr.popleft()
    cnt += 1

print(*arr)