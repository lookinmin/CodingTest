# 순서쌍의 곱의 합, 실버4, 누적 합

from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

sum_num = sum(a)
res = 0

for i in a:
    sum_num -= i
    res += sum_num * i

print(res)