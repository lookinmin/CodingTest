# 공약수, G5, 완탐-백트래킹

from sys import stdin
from math import gcd
from math import lcm
from math import sqrt


n, m = map(int, stdin.readline().split())
res = []

tmp = m // n

for i in range(int(sqrt(tmp)), 0, -1):      # 루트tmp부터 -1씩 역순으로 내려가면서
    k = int(tmp / i)
    if tmp % i == 0 and gcd(i,k) == 1:
        print(i*n, k * n)
        break


# ------------------- 시간초과 코드 -----------------------------------
# for x in range(1, m):
#     for y in range(1, m):
#         if gcd(x, y) == n and lcm(x, y) == m:
#             res.append([x,y])
#
# res.sort(key = lambda x : sum(x))
#
# print(*res[0])
