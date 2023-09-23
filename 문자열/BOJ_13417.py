# 카드 문자열, S3, 문자열

from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    num = int(stdin.readline())
    arr = list(map(str, stdin.readline().split()))
    q = deque()
    q.append(arr[0])
    # 그냥 다음문자 비교해서 나보다 앞이면 appendleft 아니면 append

    for i in range(1, len(arr)):
        tmp = q[0]
        if arr[i] > tmp:
            q.append(arr[i])
        else:
            q.appendleft(arr[i])

    for w in q:
        print(''.join(w), end='')
    print()