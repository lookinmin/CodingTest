# 소수를 분수로, S1, 수학-문자열

from sys import stdin
from math import gcd

t = int(stdin.readline().rstrip())


def make(s):
    if '(' in s:        # 순환소수
        start = s.find('(')
        end = s.find(')')
        recur = s[start + 1:end]        # 반복 되는 부분
        before = s[2:start]             # 순환하지 않는 소수부
        n1_left = 10 ** len(before + recur)
        n2_left = 10 ** len(before)
        n1_right = before + recur
        n2_right = before

        if n2_right =="":       # 모든 소수부가 순환소수라면
            n2_right = '0'

        parent = int(int(n1_left) - int(n2_left))
        child = int(int(n1_right)-int(n2_right))
    else:       # 순환 소수가 아님
        parent = int((10**(len(s[:1]) - 1)) * (10 ** (len(s[2:]))))
        child = int(s[:1] + s[2:])
    return parent, child

for _ in range(t):
    a = stdin.readline().rstrip()
    p, c = make(a)
    print("{}/{}".format(c//gcd(p,c), p//gcd(p,c)))
