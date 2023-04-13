# 소수 부분 문자열, S1, 문자열

from sys import stdin
import math

def isPrime(n):
    li = [1] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if li[i]:
            for j in range(i + i, n + 1, i):
                li[j] = 0
    p = [i for i in range(2, n + 1) if li[i]]       # 소수만 리스트에 담아서 리턴
    return p

while 1:
    res = 0
    n = int(stdin.readline().rstrip())
    m = str(n)
    if n == 0:
        exit(0)
    p = isPrime(100000)
    res = 2
    for i in p:
        if str(i) in m:
            res = i
    print(res)
