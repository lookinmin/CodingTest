# 블로그, 실버3, 누적 합

from sys import stdin

n, x = map(int, stdin.readline().split())
psum = [0 for i in range(n+1)]
a = list(map(int, stdin.readline().split()))
for i in range(1, n+1):
    psum[i] = psum[i-1] + a[i-1]
res = []
s = 0

while s + x <= n:
    res.append(psum[s+x] - psum[s])
    s += 1

if max(res) == 0:
    print("SAD")
else:
    print(max(res))
    print(res.count(max(res)))



