# 곱셈, S1, 수학

from sys import stdin

a,b,c = map(int, stdin.readline().split())

# num = (a**b)%c      # 시간초과
# print(num)

# 지수법칙과 나머지 분배 법칙을 알아햐 함
# 지수 법칙 : A^m+n = A^m * A^n
# 나머지 분배 법칙 : (AXB)%C = (A%C) X (B%C) %C
# 즉, 10^11%12 = ((10^5) %12 x (10^5) %12 x 10) % 12
# 10^5 = 10^2 * 10^2 * 10
# 분할정복 방식으로 해결 가능 //2 계속

def multi(a, b):
    if b == 1:
        return a%c
    else:
        tmp = multi(a, b//2)
        if b % 2 == 0:
            return (tmp**2) % c
        else:
            return (tmp**2 * a) % c

print(multi(a,b))
