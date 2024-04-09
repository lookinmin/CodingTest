# 풍선 터뜨리기, S3
from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque(enumerate(map(int, stdin.readline().split())))

for _ in range(n):
    idx, val = q.popleft()
    print(idx + 1, end=" ")
    if val > 0:
        q.rotate(-(val - 1))
    else:
        q.rotate(-val)