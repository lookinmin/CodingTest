# 반전 요세푸스, S3
from collections import deque

n, k, m = map(int, input().split())

q = deque(range(1, n + 1))
idx = 0

while q:
    if idx // m % 2 == 0:
        for _ in range(k - 1):
            q.append(q.popleft())
    else:
        for _ in range(k):
            q.appendleft(q.pop())
    idx += 1
    print(q.popleft())




q = [i for i in range(1, n + 1)]
removed = []

idx = 0
cnt = 0

flag = False        # False면,-> | True면, <-
while len(q) > 0:
    if cnt % m == 0:
        flag = not flag

    if flag:
        idx = (idx + k - 1) % len(q)
    else:
        idx = (idx - k) % len(q)

        while idx < 0:
            idx += len(q)
    cnt += 1
    print(q[idx])
    q.pop(idx)

