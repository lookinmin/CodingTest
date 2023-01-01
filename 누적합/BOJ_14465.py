# 소가 길을 건너간 이유5, 실버2, 누적 합
# 연속한 k개의 신호등이 존재 하도록 수리할 것

from sys import stdin

n, k, b = map(int, stdin.readline().split())
a = [0 for _ in range(n+1)]
psum = [0 for _ in range(n+1)]
for i in range(b):
    h = int(stdin.readline())
    a[h] = 1

for i in range(1, n+1):
    psum[i] = psum[i-1] + a[i]

ans = b
for j in range(k, n+1):
    ans = min(ans, psum[j] - psum[j-k])

print(ans)