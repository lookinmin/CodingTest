# 보이는 점의 개수, S2, 누적합, 수학
# x, y 가 서로 안나눠떨어지면 된다
# y % x != 0
# x % y != 0        -> gcd(x, y) == 1

from math import gcd
from sys import stdin

psum = [0 for _ in range(1001)]
psum[1] = 3
for x in range(2, 1001):
    cnt = 0
    for y in range(1, x + 1):
        if x == y:      # 절반만
            continue
        if gcd(x, y) == 1:
            cnt += 2    # y=x에 대해 대칭이니까 +2 씩
    psum[x] = psum[x-1] + cnt


C = int(stdin.readline())
for _ in range(C):
    n = int(stdin.readline())
    print(psum[n])