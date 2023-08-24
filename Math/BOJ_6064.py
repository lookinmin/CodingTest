# 카잉 달력, S1, 수학

from sys import stdin

T = int(stdin.readline())

def find(m, n, x ,y):
    res = x
    while res <= m * n:
        if (res-x) % m == 0 and (res-y) % n == 0:
            return res
        res += m
    return -1

for _ in range(T):
    m, n, x, y = map(int,stdin.readline().split())
    print(find(m, n, x, y))




