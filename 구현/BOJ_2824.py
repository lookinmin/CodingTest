# 최대공약수, S1, 구현

from sys import stdin
from math import gcd

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
a = 1
for i in arr:
    a *= i
m = int(stdin.readline())
arr2 = list(map(int, stdin.readline().split()))
b = 1
for i in arr2:
    b *= i

res = str(gcd(a, b))

if len(res) >= 9:
    print(res[-9:])
else:
    print(res)