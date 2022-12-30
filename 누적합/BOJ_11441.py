# 합 구하기, 실버3, 구간 쿼리

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.insert(0, 0)
psum = [0 for _ in range(n+1)]

for i in range(1, n+1):
    psum[i] = psum[i-1] + a[i]

for k in range(m):
    i, j = map(int, input().split())
    print(psum[j] - psum[i-1])


