# 헨리. G5, 수학-구현
# 단위분수 = 분자가 1인 분수
# 같은 단위분수가 두 개 이상 포함될 수 없으

from sys import stdin
from fractions import Fraction

T = int(stdin.readline())

# 가장 큰 단위분수 = 원래 분수에서 분자를 1로 만들었을 때 생기는 분모의 값을 올림
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    while a != 1:
        tmp = (b // a)+1        # 분자가 1인 가장 큰 단위분수의 분모
        a = a * tmp - b
        b = b * tmp
        a, b = map(int, str(Fraction(a, b)).split('/'))
    print(b)
