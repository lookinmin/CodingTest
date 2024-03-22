# 내 뒤에 나와 다른 수, S2
from sys import stdin
from collections import deque
n = int(stdin.readline())
arr = [0] + list(map(int, stdin.readline().split()))
point = deque()
for i in range(1, n):
    tmp = arr[i]
    nxt = arr[i + 1]
    if tmp != nxt:
        point.append(i + 1)

for i in range(1, n + 1):
    if len(point) == 0:
        print(-1, end=" ")
    else:
        if i < point[0]:
            print(point[0], end = " ")
        else:
            point.popleft()
            if len(point) == 0:
                print(-1, end=" ")
            else:
                print(point[0], end = " ")