# blobyum, S4, 누적합

from sys import stdin
from itertools import accumulate        # 누적합할때 사용

n ,k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
psum = [0] + list(accumulate(arr))      # for문 돌리는 psum보다 accumlate가 빠르다

res = 0

for i in range(n):
    if i+k <= n:
        res = max(res, psum[i+k] - psum[i])
    else:
        res = max(res, psum[n] - psum[i] + psum[(i+k)%n])

print(res)

