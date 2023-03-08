# 먹을 것인가 먹힐 것인가, S3, 이분 탐색

from sys import stdin

T = int(stdin.readline())

def count(arrA, arrB):
    A = sorted(arrA)
    B = sorted(arrB)
    cnt = 0
    for i in A:
        for j in B:
            if j >= i:
                continue
            if i > j:
                cnt += 1
    return cnt
for _ in range(T):
    N, M = map(int,stdin.readline().split())
    arrA = list(map(int,stdin.readline().split()))
    arrB = list(map(int, stdin.readline().split()))
    print(count(arrA, arrB))

# ------------------------------------------ bisect 사용 해결법

import bisect
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    arrA = list(map(int, stdin.readline().split()))
    arrB = list(map(int, stdin.readline().split()))
    cnt = 0
    for i in arrA:
        cnt += bisect.bisect(arrB, i-1)
    print(cnt)