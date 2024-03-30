# 타노스는 요세푸스가 밉다, S2
from collections import deque
n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
q = deque(arr)
while len(q) > 1:
    q.rotate(-1)
    for _ in range(k - 1):
        q.popleft()
        if len(q) == 1:
            break

print(q[0])
