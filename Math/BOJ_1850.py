# 최대공약수, S1, 수학-유클리드 호제법

from sys import stdin
from math import gcd
# 두 자연수의 최대 공약수 구하기
# 자연수는 1로만 이루어져있음


a ,b = map(int,stdin.readline().split())

def gcd_r(x ,y):
    if y == 0:
        return x
    else:
        return gcd_r(y, x%y)

print('1' * gcd_r(a, b))

# 메모리 오류
# A = int('1'*a)
# B = int('1'*b)
#
# BigNum = max(A,B)
# SmallNum = min(A, B)
#
# if BigNum % SmallNum == 0:
#     print(SmallNum)
# else:
#     print(1)